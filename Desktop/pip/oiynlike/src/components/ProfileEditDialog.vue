<template>
  <BaseDialog>
    <template #activator="{ activatorProps }">
      <v-btn
        icon="fas fa-pen"
        variant="text"
        size="small"
        color="primary"
        v-bind="activatorProps"
      />
    </template>
    <template #default="{ close }">
      <v-card>
        <v-card-title>
          <h1 class="text-h5 font-weight-bold" @click="close">
            <v-btn icon="fas fa-arrow-left-long" variant="flat" />
            Редактирование профиля
          </h1>
        </v-card-title>
        <v-card-item>
          <v-form @submit.prevent="handleSave" class="d-flex flex-column">
            <v-avatar size="130" class="mx-auto d-block mb-3">
              <v-img
                alt="John"
                src="https://cdn.vuetifyjs.com/images/john.jpg"
              ></v-img>
              <v-badge>
                <v-icon icon="fas fa-plus" />
              </v-badge>
            </v-avatar>
            <v-label>Имя</v-label>
            <v-text-field
              placeholder="Имя"
              variant="outlined"
              density="comfortable"
              v-model="form.first_name"
            />
            <v-label>Фамилия</v-label>
            <v-text-field
              placeholder="Фамилия"
              variant="outlined"
              density="comfortable"
              v-model="form.last_name"
            />
            <v-label>E-mail</v-label>
            <v-text-field
              placeholder="E-mail"
              variant="outlined"
              density="comfortable"
              v-model="form.email"
            />
            <v-label>О себе</v-label>
            <v-text-field
              placeholder="О себе"
              variant="outlined"
              density="comfortable"
              v-model="form.about_user"
            />
            <v-btn
              block
              variant="flat"
              size="large"
              rounded="lg"
              color="blue-darken-4"
              type="submit"
              class="align-self-end text-body-1"
              :loading="isProcessing"
            >
              Сохранить изменения
            </v-btn>
          </v-form>
        </v-card-item>
      </v-card>
    </template>
  </BaseDialog>
</template>

<script>
import { ref } from "vue";
import BaseDialog from "@/components/BaseDialog.vue";
import { useAuthStore } from "@/store/useAuthStore";
import { storeToRefs } from "pinia";
import ProfileService from "@/api/service/profileService";

export default {
  components: { BaseDialog },
  setup() {
    const authStore = useAuthStore();
    const { user } = storeToRefs(authStore);

    const form = ref({
      first_name: user.value?.first_name ?? "",
      last_name: user.value?.last_name ?? "",
      email: user.value?.email ?? "",
      about_user: user.value?.about_user ?? "",
    });

    const isProcessing = ref(false);

    async function handleSave() {
      isProcessing.value = true;

      try {
        await ProfileService.updateProfile(form.value);
        await authStore.refreshUser();
      } catch (e) {
        console.error(e);
      } finally {
        isProcessing.value = false;
      }
    }

    return {
      form,
      handleSave,
      isProcessing,
    };
  },
};
</script>
