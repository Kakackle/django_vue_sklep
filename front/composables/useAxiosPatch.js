import {ref, toValue} from 'vue';
import axios from 'axios';

export async function useAxiosPatch(url, newData){
    let token = '';
    const data = ref();
    const error = ref();
    
    const response = await axios.get(`api/get_token`)
    .then((res)=>{
        token = res.data.token;
        return axios.patch(toValue(url), newData, {
            headers: {
                'X-CSRFToken': token,
                "Content-Type": "multipart/form-data"
            },
        })
    })
    .then((res)=>{
        data.value = res.data;
    })
    .catch((err)=>{
        console.log(err);
        error.value = err;
    })

    return {data, error}
}