<script setup lang="ts">
import { onMounted } from "vue";
import http from "./api/http";
import { useRouter } from "vue-router";

const router = useRouter();

onMounted(async () => {
  const token = localStorage.getItem("token");
  if (!token) return;

  try {
    await http.get("/me");
  } catch {
    localStorage.removeItem("token");
    router.push("/login");
  }
});
</script>

<template>
  <router-view />
</template>