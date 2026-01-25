import { createRouter, createWebHistory } from "vue-router";
import Login from "../views/Login.vue";
import Quiz from "../views/Quiz.vue";
import Result from "../views/Result.vue";
import WrongBook from "../views/WrongBook.vue";



const routes = [
  {
    path: "/",
    redirect: "/login",
  },
  {
    path: "/login",
    component: Login,
  },
  {
    path: "/quiz",
    component: Quiz,
    meta: { requiresAuth: true },
  },
  {
    path: "/result",
    component: Result,
    meta: { requiresAuth: true },
  },
  {
    path: "/wrong",
    component: WrongBook,
    meta: { requiresAuth: true },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem("token");

  // 已登录用户不允许回到登录页
  if (to.path === "/login" && token) {
    next("/quiz");
    return;
  }

  // 需要登录但没 token
  if (to.meta.requiresAuth && !token) {
    next("/login");
    return;
  }

  next();
});

export default router;