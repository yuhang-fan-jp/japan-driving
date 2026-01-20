<template>
  <div>
    <h2>刷题</h2>

    <div v-for="q in questions" :key="q.id">
      <p>{{ q.content }}</p>
      <img v-if="q.image_url" :src="q.image_url" width="200" />

      <button @click="answer(q.id, true)">对</button>
      <button @click="answer(q.id, false)">错</button>
    </div>

    <button @click="submit">提交</button>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import http from "../api/http";
import { useRouter } from "vue-router";

const router = useRouter();
const questions = ref<any[]>([]);
const answers = ref<any[]>([]);

onMounted(async () => {
  const res = await http.get("/quiz/questions?limit=50");
  questions.value = res.data;
});

const answer = (id: number, value: boolean) => {
  const idx = answers.value.findIndex(a => a.question_id === id);
  if (idx >= 0) {
    answers.value[idx].answer = value;
  } else {
    answers.value.push({ question_id: id, answer: value });
  }
};

const submit = async () => {
  const res = await http.post("/quiz/submit", {
    answers: answers.value,
  });

  sessionStorage.setItem("result", JSON.stringify(res.data));
  router.push("/result");
};
</script>