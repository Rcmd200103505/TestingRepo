import axios from "axios";
import { useAuthStore } from "@/store/useAuthStore";

const axiosInstance = axios.create({
  baseURL: process.env.VUE_APP_BASE_API_URL,
});

axiosInstance.interceptors.request.use(
  (config) => {
    const authStore = useAuthStore();

    if (authStore.isLoggedIn) {
      config.headers["Authorization"] = `Bearer ${authStore.accessToken}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

axiosInstance.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default axiosInstance;
