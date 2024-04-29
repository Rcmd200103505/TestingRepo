<template>
  <div class="d-flex flex-column pa-6 h-100">
    <div class="flex-grow-1 d-flex flex-column justify-center align-center">
      <v-form class="w-100" @submit.prevent="handleLogin">
        <h1 class="text-h4 font-weight-bold mb-4">Войти</h1>
        <v-text-field
          placeholder="E-mail"
          variant="outlined"
          type="email"
          density="comfortable"
          v-model="loginForm.email"
        />
        <PasswordInput v-model="loginForm.password" />
        <v-btn
          variant="flat"
          color="blue-darken-4"
          block
          rounded="md"
          size="large"
          type="submit"
          class="text-body-1"
          :loading="isProcessing"
        >
          Войти
        </v-btn>
        <router-link
          to="/forgot-password"
          class="text-grey-darken-2 text-center text-decoration-none text-center d-block mt-4"
        >
          Забыли пароль?
        </router-link>
      </v-form>
    </div>
    <div class="text-grey-darken-2 text-center">
      Нет аккаунта?
      <router-link
        to="/register"
        class="font-weight-bold text-blue-darken-4 text-decoration-none"
      >
        Регистрация
      </router-link>
    </div>
  </div>
</template>

<script>
import PasswordInput from "@/components/PasswordInput.vue";
import { useAuthStore } from "@/store/useAuthStore";

export default {
  components: { PasswordInput },
  data() {
    return {
      isProcessing: false,
      loginForm: {
        email: "",
        password: "",
      },
    };
  },
  methods: {
    async handleLogin() {
      try {
        const data = {
          email: this.loginForm.email,
          password: this.loginForm.password,
        };

        this.isProcessing = true;

        const authStore = useAuthStore();
        await authStore.login(data);

        this.$router.push("/dashboard");
      } catch (error) {
        alert(
          "Неудачная попытка входа. Пожалуйста, проверьте свои учетные данные."
        );
      } finally {
        this.isProcessing = false;
      }
    },
  },
};
</script>
