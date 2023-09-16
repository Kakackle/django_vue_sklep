import {ref, toValue} from 'vue';
import axios from 'axios';

export async function useAxiosGetPaginated(url){
    const data = ref();
    const pages = ref();
    const error = ref();
    const count = ref();

    const response = await axios.get(toValue(url))
    .then((res)=>{
        data.value = res.data.results;
        pages.value = res.data.context.page_links;
        count.value = res.data.count;
    })
    .catch((err)=>{
        console.log(err);
        error.value = err;
    })
    return {data, pages, error, count}
}