<template>
  <v-form
    class="d-flex flex-column pa-5 h-100 w-100"
    @submit.prevent="handleRegister"
  >
    <v-progress-linear
      color="blue-darken-4"
      :model-value="progress"
      :height="8"
      class="position-absolute w-100"
    />
    <div class="flex-grow-1 d-flex flex-column justify-center align-center">
      <div class="w-100">
        <template v-if="step === 1">
          <h1 class="text-h4 mb-2 font-weight-bold">Регистрация</h1>
          <div class="text-body-2 mb-4 text-grey-darken-2 mb-4">
            Заполните ваши данные
          </div>
          <v-text-field
            placeholder="Имя"
            variant="outlined"
            density="comfortable"
            v-model="registerForm.first_name"
          />
          <v-text-field
            placeholder="Фамилия"
            variant="outlined"
            density="comfortable"
            v-model="registerForm.last_name"
          />
          <v-text-field
            placeholder="E-mail"
            variant="outlined"
            type="email"
            density="comfortable"
            v-model="registerForm.email"
          />
        </template>
        <template v-else-if="step === 2">
          <h1 class="text-h4 mb-4 font-weight-bold">
            Придумайте <br />
            пароль
          </h1>
          <PasswordInput v-model="registerForm.password" />
          <PasswordInput v-model="passwordConfirm" />
          <v-alert type="info" variant="tonal" density="compact">
            Пароль должен содержать не менее 8 символов
          </v-alert>
        </template>
      </div>
    </div>
    <div v-if="step === 1" class="text-grey-darken-2 text-center mb-5">
      Есть аккаунт?
      <router-link
        to="/auth"
        class="font-weight-bold text-blue-darken-4 text-decoration-none"
      >
        Вход
      </router-link>
    </div>
    <v-btn
      v-if="step > 1"
      variant="text"
      size="small"
      color="grey-darken-2"
      class="text-body-2 mb-5"
      @click="step -= 1"
    >
      Вернуться к предыдущему шагу
    </v-btn>
    <v-btn
      variant="flat"
      color="blue-darken-4"
      rounded="md"
      size="large"
      class="text-body-1"
      @click="nextStep"
    >
      {{ step < 2 ? "Продолжить" : "Зарегистрироваться" }}
    </v-btn>
  </v-form>
</template>

<script>
import PasswordInput from "@/components/PasswordInput.vue";
import { useAuthStore } from "@/store/useAuthStore";
import { useToastStore } from "@/store/useToastStore";

export default {
  components: { PasswordInput },
  data() {
    return {
      step: 1,
      registerForm: {
        first_name: "",
        last_name: "",
        password: "",
        email: "",
      },
      passwordConfirm: "",
    };
  },
  computed: {
    progress() {
      if (this.step === 1) {
        return 50;
      } else {
        return 100;
      }
    },
  },
  methods: {
    async handleRegister() {
      try {
        const data = {
          ...this.registerForm,
          user_type: "USER",
        };
        const authStore = useAuthStore();
        await authStore.register(data);
        useToastStore().addToast("Вы успешно зарегистрировались");
        this.$router.push("/auth");
      } catch (error) {
        useToastStore().addToast(
          error.response?.data?.error ?? "Введены некорректные данные",
          "error"
        );
      }
    },
    nextStep() {
      if (this.step === 2) {
        this.handleRegister();
        return;
      }

      this.step++;
    },
  },
};
</script>
