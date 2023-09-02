// Store for handling currently logged user
import {defineStore} from "pinia"
import {ref} from 'vue'

export const useUserStore = defineStore('user',()=>{
    const loggedUser = ref()
    const setUser = (newUser)=>{
        loggedUser.value = newUser;
    }
    const getUser = ()=>{
        return loggedUser.value;
    }
    return {loggedUser, setUser, getUser}
})