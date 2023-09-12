import { useUserStore } from "../stores/user.js"
import { storeToRefs } from "pinia";

export function useUser() {
    const userStore = useUserStore();
    const {loggedUser} = storeToRefs(userStore);
    return loggedUser
}
