import { createRouter, createWebHistory } from "vue-router";
import Login from "../views/Login.vue";
import Quiz from "../views/Quiz.vue";
import Result from "../views/Result.vue";
import WrongBook from "../views/WrongBook.vue";

const routes = [
  { path: "/", redirect: "/login" },
  { path: "/login", component: Login },
  { path: "/quiz", component: Quiz },
  { path: "/result", component: Result },
  { path: "/wrong", component: WrongBook },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;