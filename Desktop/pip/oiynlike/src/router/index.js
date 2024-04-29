import { createRouter, createWebHistory } from "vue-router";
import { useAuthStore } from "@/store/useAuthStore";
import routes from "@/router/routes";

function isAuthenticated() {
  const authStore = useAuthStore();
  return authStore.isLoggedIn;
}

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  if (
    to.matched.some((record) => record.meta.requiresAuth) &&
    !isAuthenticated()
  ) {
    next("/auth");
  } else if (
    to.matched.some((record) => record.meta.onlyNotAuth) &&
    isAuthenticated()
  ) {
    next("/");
  } else {
    next();
  }
});

export default router;
