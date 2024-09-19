import axios from 'axios'


const REGISTER_URL = "/api/v1/auth/users/"
const LOGIN_URL = 'api/v1/auth/jwt/create/'
const ACTIVATE_URL = "api/v1/auth/users/activation/"


//register user
const register = async(userData) => {
    const config = {
        headers: {
            "Content-Type": "application/json"
        },
    };

    const response = await axios.post(REGISTER_URL, userData, config)
    return response.data
}


//login user
const login = async(userData) => {
    const config = {
        headers: {
            "Content-Type": "application/json"
        },
    };
    const response = await axios.post(LOGIN_URL, userData, config)
    if(response.data){
        localStorage.setItem("user", JSON.stringify(response.data));
    }
    return response.data
}


// logout 

const logout = () => localStorage.removeItem("user");

const activate = async (userData) => {
    const config = {
        headers:{
            "Content-Type": "application/json",
        }
    };
    const reponse = await axios.post(ACTIVATE_URL, userData, config);
    return reponse.data;
}

const authService = { register, login, logout, activate}

export default authService;