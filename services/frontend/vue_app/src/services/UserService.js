import axios from 'axios'
import { SERVICE_URLS, getFullPath} from '@/config/config.js'

export default {
  
    async getUser() {
        let res = await axios.get(getFullPath(SERVICE_URLS.userUrl));
        return res.data;
    },

    async registerUser(accessToken, email) {
        let res = await axios.post(getFullPath(SERVICE_URLS.userUrl), {
            email: email
        }, {
            headers: {
                Authorization: `Bearer ${accessToken}`
            }
        });
        return res.data
    },

    async addApiKey(apiKey) {
        
    }

}