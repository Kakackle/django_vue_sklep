import {ref, watchEffect, toValue} from 'vue';
import axios from 'axios';

export async function useAxiosGet(url) {
    const data = ref();
    const error = ref();
    
    // watchEffect should watch, if any changes were commited to input url
    // if it is a ref object

    // watchEffect(()=>{
    //     // reset
    //     data.value = null;
    //     data.error = null;
    //     axios.get(toValue(url))
    //     .then((res)=>{
    //         data.value = res.data;
    //     })
    //     .catch((err)=>{
    //         console.log(err);
    //         error.value = err;
    //     })
    // })
    
    // response tylko zeby przypisac do czegos await
    const response = await axios.get(toValue(url))
    .then((res)=>{
        data.value = res.data;
    })
    .catch((err)=>{
        console.log(err);
        error.value = err;
    })
    // console.log(`data: ${JSON.stringify(data.value)}`);
    return {data, error}
}