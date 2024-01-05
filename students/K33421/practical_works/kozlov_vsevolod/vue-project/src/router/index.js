// @ означает src
import Hello from "@/components/Hello"
// import Можем называть как угодно, все равно вернется одно и то же
import Anything from "@/components/Second";

import {createRouter, createWebHistory} from "vue-router"
import Warriors from "@/views/Warriors"

const routes = [
    {
        path: '/warriors',
        component: Warriors
    }
]

const router = createRouter(({
    history: createWebHistory(), routes
}))

// Что означает это?
export default router;
