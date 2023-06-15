<template>
  <div>
    <form @submit.prevent="createPost">
      <input
        type="datetime-local"
        name="date"
        id="date"
        v-model="formData.date"
      />
      <input
        class="name"
        type="text"
        placeholder="Заголовок"
        v-model="formData.name"
      />
      <input
        type="text"
        name="description"
        id="description"
        v-model="formData.description"
      />
      <!-- <component :is="editor" v-model="formData.description"></component> -->
      <button class="publish">Опубликовать</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import Editor from "./Editor.vue";

const headers = { "Content-Type": "application/json; charset=UTF-8" };

export default {
  components: {
    Editor,
  },
  data() {
    return {
      editor: "Editor",
      formData: {
        date: "",
        // tags: ["Тест", "Мода"],
        // keywords: [],
        name: "",
        description: "",
        // image: "",
      },
    };
  },
  methods: {
    createPost() {
      axios
        .post("http://localhost:8000/api/news/", this.formData, {
          headers: headers,
        })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  // mounted() {
  //   this.postArticles();
  // },
};
</script>

<style scoped>
.publish {
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
.publish:hover {
  background: grey;
  color: #fff;
  transition: 0.2s;
}
.publish.selected {
  background: #000;
  color: #fff;
}
.name {
  width: -webkit-fill-available;
  padding: 1em;
  border-width: 1px;
  border-style: solid;
  border-color: #ccced1;
}
.name:focus {
  box-shadow: rgb(204, 219, 232) 3px 3px 6px 0px inset,
    rgba(255, 255, 255, 0.5) -3px -3px 6px 1px inset;
  outline-width: thin;
  outline-style: solid;
  outline-color: #6cb5f9;
  outline-offset: -1px;
}
</style>
