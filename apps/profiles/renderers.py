import json

from rest_framework.renderers import JSONRenderer

class ProfileJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        errors = data.get('errors', None)

        if errors is not None:
            return super(ProfileJSONRenderer, self).render(data)

        return json.dumps({"profile": data})


class ProfilesJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        # If the data is a dictionary (for single object responses), check for 'errors'
        if isinstance(data, dict):
            errors = data.get('errors', None)

            if errors is not None:
                return super(ProfilesJSONRenderer, self).render(data)

            # For single profile object, wrap in "profile"
            return json.dumps({"profile": data})
        
        # If the data is a list (for multiple object responses), wrap in "profiles"
        elif isinstance(data, list):
            return json.dumps({"profiles": data})
        
        return super(ProfilesJSONRenderer, self).render(data)