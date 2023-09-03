import { createRouter, createWebHistory, createWebHashHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AboutView from "../views/AboutView.vue";
import ProductView from "../views/ProductView.vue";

const router = createRouter({
    base: 'sklep/',
    history: createWebHistory('sklep/'),
    routes:[
        {
            path: "/",
            name: "home",
            component: HomeView,
            meta: {
                desc: "Home view",
                title: "Home",
            },
        },
        {
            path: "/product/:product_slug?",
            name: "product",
            component: ProductView,
            meta: {
                desc: "Product view",
                title: "Product",
            },
        },
        {
            path: "/about",
            name: "about",
            component: AboutView,
            meta: {
                desc: "About author/project page + site map?",
                title: "About",
            },
        }
    ]
})

router.beforeEach((to, from, next) => {
    // Get the page title from the route meta data that we have defined
    // See further down below for how we setup this data
    const title = to.meta.title;
    // If the route has a title, set it as the page title of the document/page
    if (title) {
      document.title = title + " | Vue Blog";
    }
    // Continue resolving the route
    next();
  });

export default router;