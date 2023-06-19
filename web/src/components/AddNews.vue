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
      <div id="editor">
        <ckeditor
          :editor="editor"
          v-model="formData.description"
          :config="editorConfig"
        ></ckeditor>
      </div>
      <label for="thumbnail">Обложка новости</label>
      <input
        type="file"
        name="thumbnail"
        id="thumbnail"
        @change="uploadImage"
        accept="image/*"
      />
      <button class="publish">Опубликовать</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import { ClassicEditor } from "@ckeditor/ckeditor5-editor-classic";
import { ImageUpload } from "@ckeditor/ckeditor5-image";
import { SimpleUploadAdapter } from "@ckeditor/ckeditor5-upload";
import { Essentials } from "@ckeditor/ckeditor5-essentials";
import { Bold, Italic } from "@ckeditor/ckeditor5-basic-styles";
import { Link } from "@ckeditor/ckeditor5-link";
import { Paragraph } from "@ckeditor/ckeditor5-paragraph";

const options = {
  headers: { "Content-Type": "multipart/form-data; charset=UTF-8" },
};

export default {
  name: "editor",
  data() {
    return {
      editor: ClassicEditor,
      //editorData: "<p>Content of the editor.</p>",
      editorConfig: {
        placeholder: "Текст Вашей новости.",
        plugins: [
          ImageUpload,
          SimpleUploadAdapter,
          Essentials,
          Bold,
          Italic,
          Link,
          Paragraph,
        ],

        toolbar: {
          items: [
            "bold",
            "italic",
            // "imageUpload",
            "link",
            "undo",
            "redo",
          ],
        },

        imageUpload: {
          isEnabled: true,
        },

        simpleUpload: {
          uploadUrl: "http://localhost:8000/upload/images",
        },
      },
      formData: {
        date: "",
        //tags: ["Тест", "Мода"],
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
        .post("http://localhost:8000/api/news/", this.formData, options)
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
