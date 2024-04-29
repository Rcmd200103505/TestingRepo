import authService from "@/api/service/authService";
import { defineStore } from "pinia";
import { computed, ref } from "vue";
import ProfileService from "@/api/service/profileService";

export const useAuthStore = defineStore(
  "auth",
  () => {
    const accessToken = ref(null);
    const user = ref(null);

    const userFullname = computed(() =>
      user.value != null
        ? user.value.first_name + " " + user.value.last_name
        : ""
    );
    const isLoggedIn = computed(() => !!accessToken.value);

    async function refreshUser() {
      const data = await ProfileService.fetchProfile();
      user.value = data.user;
    }

    async function login(credentials) {
      const data = await authService.login(credentials);
      user.value = data;
      accessToken.value = data.token;
    }
    async function register(userData) {
      const data = await authService.register(userData);
      user.value = data;
      accessToken.value = data.token;
    }

    function logout() {
      user.value = null;
      accessToken.value = null;
    }

    return {
      accessToken,
      user,
      isLoggedIn,
      login,
      register,
      userFullname,
      refreshUser,
      logout,
    };
  },
  {
    persist: {
      paths: ["user", "accessToken"],
    },
  }
);
