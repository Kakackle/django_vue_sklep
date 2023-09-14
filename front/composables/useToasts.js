import {ref, toValue} from 'vue';
import { useToast } from 'vue-toastification';
const toast = useToast();

export async function useToasts(data, error, succes_msg, error_msg){
    if(data.value){
        // console.log(JSON.stringify(data.value))
        // if (data.value.status === 400)
        // {
        //     toast.error(data.value.message);
        // }
        toast.success(succes_msg);
    }
    if(error.value){
        // if(error.value.message){
        //     toast.error(error.value.message);    
        // }
        // else{
        //     toast.error(error_msg);
        // }
        toast.error(error_msg);
    }
}