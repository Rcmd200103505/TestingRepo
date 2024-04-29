<template>
  <ul class="bg-blue-darken-4 rounded-xl d-flex justify-space-around py-3">
    <li
      v-for="(item, index) in items"
      :key="index"
      @click="setActiveTab(item, index)"
    >
      <component
        :is="item.to ? 'router-link' : 'span'"
        class="rounded-xl py-1 px-5 text-decoration-none"
        :class="
          activeTabIndex === index
            ? 'bg-white text-blue-darken-4'
            : 'text-white bg-blue-darken-4'
        "
        v-if="item.to"
        :to="item.to"
      >
        {{ item.text }}
      </component>
    </li>
  </ul>
</template>

<script>
import { onMounted, ref } from "vue";
import { useRoute } from "vue-router";

export default {
  props: {
    items: {
      type: Array,
      default: () => [],
    },
  },
  setup(props, { emit }) {
    const activeTabIndex = ref(0);
    const route = useRoute();

    function setActiveTab(item, index) {
      activeTabIndex.value = index;
      emit("change", item);
    }

    onMounted(() => {
      activeTabIndex.value =
        props.items.findIndex((item) => route.path === item.to) ?? 0;
    });

    return {
      activeTabIndex,
      setActiveTab,
    };
  },
};
</script>
