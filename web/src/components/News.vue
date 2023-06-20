<template>
  <!-- Контейнер карточек -->
  <div class="card__container">
    <!-- Карточки -->
    <div v-if="selectedNews">
      <button class="back-button" v-on:click="backToList">Назад</button>
      <div class="selected-news">
        <h1>{{ selectedNews.name }}</h1>
        <div v-html="selectedNews.description"></div>
      </div>
    </div>
    <div v-else>
      <input
        class="search"
        type="text"
        v-model="searchQuery"
        placeholder="Введите запрос"
      />
      <div
        v-for="item in searchedItems"
        :key="item.id"
        @click="showNews(item)"
        class="card"
      >
        <div class="thumbnail__container">
          <img class="thumbnail" :src="item.image" />
        </div>
        <div class="title-description__container">
          <p сlass="date">{{ item.date }}</p>
          <a class="title">{{ item.name }}</a>
          <div class="description">
            {{
              item.description
                ? item.description.slice(0, 200).replace(/(<([^>]+)>)/gi, "")
                : ""
            }}
          </div>
          <p class="tags">
            <span v-for="tag in item.tags"> #{{ tag }} </span>
          </p>
          <p class="keywords">
            <span v-for="keyword in item.keywords"> #{{ keyword }} </span>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { computed, onMounted, reactive, Ref, ref } from "vue";

interface Tag {
  name: string;
}

interface Keywords {
  name: string;
}

interface News {
  id: number;
  date: string;
  name: string;
  description: string;
  tags: Tag[];
  keywords: Keywords[];
  image: string;
}

export default {
  setup(): {
    searchedItems: any;
    searchQuery: { value: string };
    selectedNews: any;
    showNews: (item: News) => void;
    backToList: () => void;
  } {
    const items = reactive<News[]>([]);
    const searchQuery = ref("");
    const selectedNews: Ref<any> =
      ref(null);
    const showNews = (item: News): void => {
      selectedNews.value = item;
    };
    const backToList = (): void => {
      selectedNews.value = null;
    };
    const searchedItems = computed(() => {
      return items.filter((item: News) => {
        return (
          item.name.toLowerCase().indexOf(searchQuery.value.toLowerCase()) != -1
        );
      });
    });
    onMounted(async () => {
      try {
        const response = await fetch("http://localhost:8000/api/news/");
        const data = await response.json();
        data.forEach((item: News) => {
          items.push(item);
        });
      } catch (e) {
        console.log("Ошибка загрузки новостей");
      }
    });
    return { searchedItems, searchQuery, selectedNews, showNews, backToList };
  },
};
</script>

<style scoped>
.back-button {
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
.back-button:hover {
  background: grey;
  color: #fff;
  transition: 0.2s;
}
.back-button.selected {
  background: #000;
  color: #fff;
}
.selected-news {
  background-color: #fff;
  overflow: hidden;
  margin: 1em;
  padding: 1em;
  border-radius: 1em;
}
.search {
  padding: 1em;
  border-width: 1px;
  border-radius: 1em;
  border-style: solid;
  border-color: #ccced1;
}
.search:focus {
  box-shadow: rgb(204, 219, 232) 3px 3px 6px 0px inset,
    rgba(255, 255, 255, 0.5) -3px -3px 6px 1px inset;
  outline-width: thin;
  outline-style: solid;
  outline-color: #6cb5f9;
  outline-offset: -1px;
}

.card__container {
  display: flex;
  flex-direction: column;
}
.card {
  display: flex;
  flex-direction: row;
  background-color: #fff;
  overflow: hidden;
  margin: 1em;
  border-radius: 1em;
}
.thumbnail__container {
  width: 50%;
}
.thumbnail {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.title-description__container {
  margin: 1em;
}
.date {
  color: rgb(240, 242, 245);
}
.title {
  font-weight: bold;
}
.description {
}
@media only screen and (max-width: 720px) {
  .card {
    flex-direction: column !important;
  }
  .thumbnail__container {
    width: 100%;
  }
}
</style>
