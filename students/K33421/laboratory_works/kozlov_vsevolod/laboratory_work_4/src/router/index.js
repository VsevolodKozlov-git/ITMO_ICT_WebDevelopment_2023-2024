import {createRouter, createWebHistory} from "vue-router"
import ReaderRareBooks from "@/views/ReaderRareBooks";
import ReaderOutdated from "@/views/ReaderOutdated"
import ReaderBookMonthAgo from "@/views/ReaderBookMonthAgo"
import ReaderCreate from "@/views/ReaderCreate"
import Statistics from "@/views/Statistic"
import TestPage from "@/views/TestPage"
import BookInstanceList from "@/views/BookInstanceList"
import BookInstanceUpdate from "@/views/BookInstanceUpdate"
import UserLogin from "@/views/UserLogin"
import UserUpdate from "@/views/UserUpdate"
import UserRegistration from "@/views/UserRegistration"

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
        path:'/book_instance/update/:pk',
        component: BookInstanceUpdate
    },
    {
        path: '/test_page',
        component: TestPage
    },
    {
        path: '/user/login',
        component: UserLogin
    },
    {
        path: '/user/update',
        component: UserUpdate
    },
    {
        path: '/user/registration',
        component: UserRegistration
    }
]

const router = createRouter(({
    history: createWebHistory(), routes
}))

export default router;
