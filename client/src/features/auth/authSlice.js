import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import authService from "./autService";


const user = JSON.parse(localStorage.getItem('user'));

const initialState =  {
    user: user ? user: null,
    isError: false,
    isLoading: false,
    isSuccess: false,
    message: "",
};


export const register = createAsyncThunk(
    "auth/register",
    async(user, thunkAPI) => {
        try{
            return await authService.register(user)
        }catch(error){
            const message = (error.resppnse && error.reponse.data && error.response.data.message) ||
            error.message || error.toString();

            return thunkAPI.rejectWithValue(message)
        }

    }
)


export const login = createAsyncThunk(
    "auth/login", async (user, thunkAPI) => {
        try {
            const response = await authService.login(user);
            // localStorage.setItem('user', JSON.stringify(response.data));
            return response.data;
        } catch (error) {
            const message =
                (error.response && error.response.data && error.response.data.message) ||
                error.message ||
                error.toString();
            return thunkAPI.rejectWithValue(message);
        }
    }
)


export const logout = createAsyncThunk(
    "auth/logout", async () => {
        authService.logout();
    }
)


export const activate = createAsyncThunk(
    "auth/activate", async (user, thunkAPI) => {
        try{
            return await authService.activate(user);
        }catch(e){
            const message = (e.resppnse && e.reponse.data && e.response.data.message) ||
            e.message || e.toString();
            return thunkAPI.rejectWithValue(message)
        }
    }
)


export const authSlice = createSlice({
    name: "auth",
    initialState,
    reducers: {
        reset(state) {
            state.user = null;
            state.isLoading = false;
            state.isError = false;
            state.isSuccess = false;
            state.message = "";
        },
        setAuth(state, action) {
            state.user = action.payload;
            state.isLoading = false;
            state.isError = false;
            state.isSuccess = true;
            state.message = "Login Successful";
        },
        setLoading(state, action) {
            state.isLoading = action.payload;
            state.isError = false;
            state.isSuccess = false;
        },
        setError(state, action) {
            state.isLoading = false;
            state.isError = true;
            state.isSuccess = false;
            state.message = action.payload;
        },
    },
    extraReducers: (builder) => {
        builder
            .addCase(register.pending, (state) => {
                state.isLoading = true;
            })
            .addCase(register.fulfilled, (state) => {
                state.isLoading = false;
                state.isSuccess = true;
                state.message = "Registration Successful";
            })
            .addCase(register.rejected, (state, action) => {
                state.isLoading = false;
                state.isError = true;
                state.message = action.payload;
                state.user = null;
            })

            //login
            .addCase(login.pending, (state) => {
                state.isLoading = true;
            })
            .addCase(login.fulfilled, (state, action) => {
                state.isLoading = false;
                state.isSuccess = true;
                state.message = "Login Successful";
                state.user = action.payload;
            })
            .addCase(login.rejected, (state, action) => {
                state.isLoading = false;
                state.isError = true;
                state.message = action.payload;
                state.user = null;
            })

            // logout

            .addCase(logout.fulfilled, (state) => {
                state.user = null;
                state.isLoading = false;
                state.isError = false;
                state.isSuccess = true;
                state.message = "Logout Successful";
            })
            // activation

            .addCase(activate.pending, (state) => {
                state.isLoading = true;
            })
            .addCase(activate.fulfilled, (state) => {
                state.isLoading = false;
                state.isSuccess = true;
                state.message = "Account Activated";
            })
            .addCase(activate.rejected, (state, action) => {
                state.isLoading = false;
                state.isError = true;
                state.message = action.payload;
                state.user = null;
            })
    }
})

export const { reset, setAuth, setLoading, setError } = authSlice.actions;
export default authSlice.reducer;