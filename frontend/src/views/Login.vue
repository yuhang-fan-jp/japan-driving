<template>
  <div>
    <h2>登录</h2>

    <input v-model="email" placeholder="email" />
    <input v-model="password" type="password" placeholder="password" />

    <button @click="login">登录</button>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import http from "../api/http";
import { useRouter } from "vue-router";

const email = ref("");
const password = ref("");
const router = useRouter();

const login = async () => {
  try {
    const res = await http.post("/login", {
      email: email.value,
      password: password.value,
    });

    localStorage.setItem("token", res.data.access_token);
    router.push("/quiz");
  } catch (err) {
    console.error(err);
    alert("登录失败");
  }
};
</script>