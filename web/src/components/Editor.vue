<template>
  <!-- <input placeholder="Название статьи" /> -->
  <div id="editor">
    <ckeditor
      :editor="editor"
      v-model="editorData"
      :config="editorConfig"
    ></ckeditor>
  </div>
  <!-- <button>Отправить</button> -->
</template>

<script>
//import CKEditor from "@ckeditor/ckeditor5-vue";
import ClassicEditor from "@ckeditor/ckeditor5-build-classic";

export default {
  name: "editor",
  data() {
    return {
      editor: ClassicEditor,
      editorData: "<p>Текст Вашей новости.</p>",
      editorConfig: {
        // The configuration of the rich-text editor.
      },
    };
  },
};
</script>
