<script setup lang="ts">
import { ref } from "vue";
import Tabs from "./components/Tabs.vue";
import Header from "./components/Header.vue";
import News from "./components/News.vue";
import Editor from "./components/Editor.vue";
import AddNews from "./components/AddNews.vue";

const tabs = [
  { name: "News", label: "Список новостей" },
  { name: "AddNews", label: "Добавить новость" },
];

const selectedTab = ref("News");
const changeTab = (tabName) => {
  selectedTab.value = tabName;
};
</script>

<template>
  <Tabs :names="tabs" :selectedTab="selectedTab" @changeTab="changeTab">
    <div v-if="selectedTab === 'News'">
      <News />
    </div>
    <div v-if="selectedTab === 'AddNews'">
      <AddNews />
    </div>
  </Tabs>
</template>

<style></style>
