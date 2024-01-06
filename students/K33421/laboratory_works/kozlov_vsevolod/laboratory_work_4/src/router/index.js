import {createRouter, createWebHistory} from "vue-router"
import ReaderRareBooks from "@/views/ReaderRareBooks";
import ReaderOutdated from "@/views/ReaderOutdated"
import ReaderBookMonthAgo from "@/views/ReaderBookMonthAgo"
import ReaderCreate from "@/views/ReaderCreate"
import Statistics from "@/views/Statistic"
import BookInstanceList from "@/views/BookInstanceList"
import TestPage from "@/views/TestPage";

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
    },
    {
        path: '/reader/create',
        component: ReaderCreate
    },
    {
        path: '/statistics',
        component: Statistics
    },
    {
        path: '/book_instance/list',
        component: BookInstanceList
    },
    {
        path:'/test_page',
        component: TestPage
    }
]

const router = createRouter(({
    history: createWebHistory(), routes
}))

export default router;
