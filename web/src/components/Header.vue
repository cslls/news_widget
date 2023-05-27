<template>
  <div>
    <div class="tabs">
      <ul>
        <li
          v-for="(tab, index) in tabs"
          :key="index"
          :class="{ 'is-active': activeTab === tab }"
          @click="activeTab = tab"
        >
          {{ tab }}
        </li>
      </ul>
    </div>

    <div class="tab-content">
      <div
        v-for="(tabContent, index) in tabContents"
        :key="index"
        v-show="activeTab === tabContent"
      >
        {{ tabContent }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tabs: ["Tab 1", "Tab 2", "Tab 3"],
      tabContents: ["Tab 1 Content", "Tab 2 Content", "Tab 3 Content"],
      activeTab: "Tab 1",
    };
  },
};
</script>

<style scoped>
.tabs {
  display: flex;
}

.tabs ul {
  display: flex;
  list-style-type: none;
}

.tabs ul li {
  margin-right: 10px;
  padding: 5px;
}

.tab-content div {
  display: none;
}
</style>
