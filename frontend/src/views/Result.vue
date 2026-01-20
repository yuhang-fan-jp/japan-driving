<template>
  <div v-if="result">
    <h2>成绩</h2>
    <p>{{ result.score }} / {{ result.total }}</p>

    <button @click="goWrong">查看错题</button>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";

const router = useRouter();
const result = JSON.parse(sessionStorage.getItem("result") || "null");

const goWrong = () => {
  router.push("/wrong");
};
</script>