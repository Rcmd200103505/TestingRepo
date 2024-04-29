<template>
  <div class="d-flex justify-space-between align-center mb-3">
    <div class="text-blue-darken-4 text-body-1 font-weight-bold">
      {{ game.title }}
    </div>
    <div class="text-grey-darken-2 text-caption">#{{ game.title }}</div>
  </div>
  <div class="d-flex justify-space-between align-center">
    <div class="d-flex align-center">
      <v-icon icon="far fa-calendar" color="primary" />
      <span class="ml-2 text-body-2">{{ date }}</span>
    </div>
    <div class="d-flex align-center">
      <v-icon icon="fas fa-earth-americas" color="primary" />
      <span class="ml-2 text-body-2">{{ "Алматы" }}</span>
    </div>
  </div>
  <template v-if="showDescription">
    <div class="text-blue-darken-4 text-body-1 font-weight-bold my-3">
      Об игре
    </div>
    <div class="elevation-2 text-body-2 pa-3 rounded-lg">
      {{ game.description }}
    </div>
  </template>
  <div class="mt-3 d-flex align-center justify-space-between">
    <div v-if="game.matched_players.length" class="d-flex align-center">
      <v-avatar
        v-for="player in playersPreview"
        :key="player.user_id"
        color="blue-darken-4"
        size="35"
      >
        <span class="text-body-2">
          {{ player.first_name[0] + player.last_name[0] }}
        </span>
      </v-avatar>
      <span v-if="playersCount" class="text-body-2">
        + {{ playersCount }} игроков
      </span>
    </div>
    <span v-else class="text-body-2"> Нет игроков </span>
    <slot name="join" :game="game" />
  </div>
</template>

<script>
import { computed } from "vue";
import DateUtil from "@/utils/DateUtil";

export default {
  props: {
    game: {
      type: Object,
      required: true,
    },
    showDescription: {
      type: Boolean,
      default: false,
    },
  },
  setup(props) {
    const date = computed(() => DateUtil.formatDate(props.game.scheduled_time));

    const playersPreview = computed(() =>
      props.game.matched_players.slice(0, 3)
    );

    const playersCount = computed(() =>
      props.game.matched_players.length > 3
        ? props.game.matched_players.length - 3
        : 0
    );

    return { date, playersPreview, playersCount };
  },
};
</script>
