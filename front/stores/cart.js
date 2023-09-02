// Store for handling currently logged user
import {defineStore} from "pinia"
import {ref} from 'vue'

export const useCartStore = defineStore('cart',()=>{
    const cartItems = ref()
    // const setUser = (newUser)=>{
    //     loggedUser.value = newUser;
    // }
    // const getUser = ()=>{
    //     return loggedUser.value;
    // }
    return {cartItems}
})