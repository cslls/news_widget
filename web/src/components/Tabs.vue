<script setup lang="ts">
const props = defineProps({
  names: {
    type: Array,
    required: true,
  },
  selectedTab: {
    type: String,
    required: false,
  },
});
const emit = defineEmits(["changeTab"]);
const clickOnTab = (tabName) => {
  emit("changeTab", tabName);
};
</script>

<template>
  <div class="tab-nav">
    <span
      v-for="tab in names"
      :key="tab.name"
      :class="['tab-nav__item', { selected: tab.name === selectedTab }]"
      @click="clickOnTab(tab.name)"
      >{{ tab.label }}
    </span>
  </div>
  <div class="tab-content">
    <slot />
  </div>
</template>

<style scroped>
.tab-nav {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}
.tab-nav__item {
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 10px;
  border-radius: 7px;
  cursor: pointer;
  border: 1px solid #000;
  background: #fff;
  padding: 0 20px;
  font-size: 15px;
}
.tab-nav__item:hover {
  background: grey;
  color: #fff;
  transition: 0.2s;
}
.tab-nav__item.selected {
  background: #000;
  color: #fff;
}
</style>
