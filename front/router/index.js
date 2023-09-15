import { createRouter, createWebHistory, createWebHashHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AboutView from "../views/AboutView.vue";
import ProductView from "../views/ProductView.vue";
import StoreView from "../views/StoreView.vue";
import CartView from "../views/CartView.vue";
import FavouriteView from "../views/FavouriteView.vue";
import UserView from "../views/UserView.vue";
import UserListView from "../views/UserListView.vue";
import ManufacturerView from "../views/ManufacturerView.vue";
import OrderView from "../views/OrderView.vue";
import ManufacturerListView from "../views/ManufacturerListView.vue";
import NotFoundView from "../views/NotFoundView.vue";

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
            path: "/products/:product_slug?",
            name: "product",
            component: ProductView,
            meta: {
                desc: "Product view",
                title: "Product",
            },
        },
        {
            path: "/store",
            name: "store",
            component: StoreView,
            meta: {
                desc: "Store view",
                title: "Store",
            },
        },
        {
            path: "/cart",
            name: "cart",
            component: CartView,
            meta: {
                desc: "Cart view",
                title: "Cart",
            },
        },
        {
            path: "/favourite",
            name: "favourite",
            component: FavouriteView,
            meta: {
                desc: "Favourite view",
                title: "Favourite",
            },
        },
        {
            path: "/users/list",
            name: "users",
            component: UserListView,
            meta: {
                desc: "User list view",
                title: "Users",
            },
        },
        {
            path: "/users/:user_slug?",
            name: "user",
            component: UserView,
            meta: {
                desc: "User view",
                title: "User",
            },
        },
        {
            path: "/manufacturers/list",
            name: "manufacturers",
            component: ManufacturerListView,
            meta: {
                desc: "Manuf list view",
                title: "Manufacturers",
            },
        },
        {
            path: "/manufacturers/:man_slug?",
            name: "manufacturer",
            component: ManufacturerView,
            meta: {
                desc: "Manuf view",
                title: "Manufacturer",
            },
        },
        {
            path: "/orders/:order_pk?",
            name: "order",
            component: OrderView,
            meta: {
                desc: "Order view",
                title: "Order",
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
        },
        {
            path: "/:pathMatch(.*)*",
            name: "catchall",
            component: NotFoundView,
            meta: {
              desc: "Catchall for errors, will try to display input params",
              title: "Error",
            },
        },
    ]
})

router.beforeEach((to, from, next) => {
    // Get the page title from the route meta data that we have defined
    // See further down below for how we setup this data
    const title = to.meta.title;
    // If the route has a title, set it as the page title of the document/page
    if (title) {
      document.title = title + " | Kalopsia";
    }
    // Continue resolving the route
    next();
  });

export default router;