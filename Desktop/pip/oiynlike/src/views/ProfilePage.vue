<template>
  <div>
    <div class="d-flex justify-space-between align-center mb-5">
      <h1 class="text-h5 font-weight-bold">Профиль</h1>
      <v-btn
        icon="fas fa-arrow-right-from-bracket"
        variant="text"
        @click="handleLogout"
      />
    </div>
    <v-avatar size="130" class="mx-auto d-block mb-2">
      <v-img alt="John" src="https://cdn.vuetifyjs.com/images/john.jpg"></v-img>
    </v-avatar>
    <h2 class="text-h5 font-weight-bold text-center">{{ userFullname }}</h2>
    <div class="d-flex justify-space-between align-center">
      <h4 class="text-blue-darken-4 font-weight-bold text-h6">О себе</h4>
      <ProfileEditDialog />
    </div>
    <p v-if="user?.about_user.length > 0">{{ user.about_user }}</p>
    <p v-else class="text-grey-darken-2">Нет описания пользователя</p>
    <h4 class="mt-4 text-blue-darken-4 font-weight-bold text-h6">Игры</h4>
  </div>
</template>

<script>
import { useAuthStore } from "@/store/useAuthStore";
import { storeToRefs } from "pinia";
import ProfileEditDialog from "@/components/ProfileEditDialog.vue";
import { useRouter } from "vue-router";

export default {
  components: { ProfileEditDialog },
  setup() {
    const authStore = useAuthStore();
    const { user, userFullname } = storeToRefs(authStore);
    const router = useRouter();

    function handleLogout() {
      authStore.logout();
      router.push("/auth");
    }

    return {
      user,
      userFullname,
      handleLogout,
    };
  },
};
</script>
