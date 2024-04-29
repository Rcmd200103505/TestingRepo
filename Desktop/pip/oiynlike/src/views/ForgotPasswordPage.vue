<template>
  <v-form
    class="d-flex flex-column pa-5 h-100 w-100 justify-center align-center"
    @submit.prevent="handleResetPassword"
  >
    <div class="w-100">
      <h1 class="text-h4 mb-4 font-weight-bold">Сброс пароля</h1>
      <PasswordInput v-model="password" />
      <PasswordInput v-model="passwordConfirm" />
      <v-btn
        variant="flat"
        color="blue-darken-4"
        rounded="md"
        size="large"
        class="w-100 mb-4"
        b
        @click="handleResetPassword"
      >
        Восстановить
      </v-btn>
      <router-link
        to="/auth"
        class="text-grey-darken-2 text-decoration-none text-center d-block"
      >
        Войти в аккаунт
      </router-link>
    </div>
  </v-form>
</template>

<script>
import PasswordInput from "@/components/PasswordInput.vue";
import { useAuthStore } from "@/store/useAuthStore";

export default {
  components: { PasswordInput },
  data() {
    return {
      password: "",
      passwordConfirm: "",
    };
  },
  methods: {
    async handleResetPassword() {
      try {
        const data = {
          password: this.password,
        };
        await useAuthStore().register(data);
      } catch (error) {
        alert(
          "Этот адрес электронной почты уже существует. Пожалуйста, используйте другую."
        );
      }
    },
  },
};
</script>
