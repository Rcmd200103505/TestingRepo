export default [
  {
    path: "/auth",
    name: "auth",
    component: () => import("@/views/AuthorizationPage.vue"),
    meta: {
      onlyNotAuth: true,
    },
  },
  {
    path: "/register",
    name: "register",
    component: () => import("@/views/RegistrationPage.vue"),
    meta: {
      onlyNotAuth: true,
    },
  },
  {
    path: "/forgot-password",
    name: "forgot-password",
    component: () => import("@/views/ForgotPasswordPage.vue"),
    meta: {
      onlyNotAuth: true,
    },
  },
  {
    path: "/dashboard",
    name: "dashboard",
    alias: "/",
    redirect: { name: "dashboard.recommended" },
    component: () => import("@/views/dashboard/DashboardPage.vue"),
    meta: { requiresAuth: true, layout: "BaseLayout" },
    children: [
      {
        path: "user",
        name: "dashboard.user",
        component: () => import("@/views/dashboard/UserGamesPage.vue"),
        meta: { requiresAuth: true, layout: "BaseLayout" },
      },
      {
        path: "recommended",
        name: "dashboard.recommended",
        component: () => import("@/views/dashboard/RecommendedGamesPage.vue"),
        meta: { requiresAuth: true, layout: "BaseLayout" },
      },
    ],
  },
  {
    path: "/profile",
    name: "profile",
    component: () => import("@/views/ProfilePage.vue"),
    meta: { requiresAuth: true, layout: "BaseLayout" },
  },
  {
    path: "/map",
    name: "map",
    component: () => import("@/views/MapPage.vue"),
    meta: { requiresAuth: true, layout: "BaseLayout" },
  },
];
