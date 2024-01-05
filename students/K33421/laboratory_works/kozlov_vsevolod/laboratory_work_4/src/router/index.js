import {createRouter, createWebHistory} from "vue-router"
import ReaderRareBooks from "@/views/ReaderRareBooks";
import ReaderOutdated from "@/views/ReaderOutdated"
import ReaderBookMonthAgo from "@/views/ReaderBookMonthAgo"

const routes = [
    {
        path: '/reader/rare_books',
        component: ReaderRareBooks
    },
    {
        path: '/reader/outdated',
        component: ReaderOutdated
    },
    {
        path: '/reader/book_month_ago',
        component: ReaderBookMonthAgo
    }
]

const router = createRouter(({
    history: createWebHistory(), routes
}))

export default router;
