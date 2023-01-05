<template>
  <div class="auth-wrapper auth-v1 px-2">
    <div class="surface-card p-4 shadow-2 border-round w-full lg:w-6">
      <div class="text-center mb-5">
        <!-- <img src="../../assets/images/superteia.png" alt="Image" class="mb-3"> -->
        <div class="text-900 text-3xl font-medium mb-3">Welcome Back</div>
        <span class="text-600 font-medium line-height-3"
          >Don't have an account?</span
        >
        <a class="font-medium no-underline ml-2 text-blue-500 cursor-pointer"
          >Create today!</a
        >
      </div>

      <form v-on:submit="login">
        <div class="p-inputgroup mb-4">
          <span class="p-inputgroup-addon">
            <i class="pi pi-user"></i>
          </span>
          <InputText v-model="email" />
        </div>

        <div class="p-inputgroup mb-4">
          <span class="p-inputgroup-addon">
            <i class="pi pi-key"></i>
          </span>
          <Password v-model="password" />
        </div>

        <div class="flex align-items-center justify-content-between mb-6">
          <div class="flex align-items-center">
            <Checkbox
              id="rememberme1"
              :binary="true"
              v-model="checked"
              class="mr-2"
            ></Checkbox>
            <label for="rememberme1">Remember me</label>
          </div>
          <a
            class="font-medium no-underline ml-2 text-blue-500 text-right cursor-pointer"
            >Forgot password?</a
          >
        </div>

        <Button label="Sign In" icon="pi pi-user" class="w-full" type="submit"></Button>
      </form>
    </div>
  </div>
</template>

<script setup>

import { ref, computed } from 'vue';
import { required, helpers   } from "@vuelidate/validators";
import { useVuelidate } from "@vuelidate/core";
import InputText from 'primevue/inputtext';
import Checkbox from 'primevue/checkbox';
import { useAuthStore } from '@/store/auth';
const configure = useAuthStore()
const email = ref()
const password = ref()
const checked = ref()
const rules = computed(() => ({
  email: {  required: helpers.withMessage('This field cannot be empty', required) },
  password: {  required: helpers.withMessage('This field cannot be empty', required) },
    }))
const v$ = useVuelidate(rules, { email, password })
const login = (e) => {
  e.preventDefault()
  configure.login(email.value,password.value)
} 

</script>

<style scoped>
.auth-wrapper {
  display: flex;
  flex-basis: 100%;
  min-height: 100vh;
  min-height: calc(var(--vh, 1vh) * 100);
  width: 100%;
}
.auth-wrapper.auth-v1 {
  align-items: center;
  justify-content: center;
  overflow: hidden;
}
.auth-wrapper.auth-v1 .auth-inner {
  max-width: 400px;
}
.auth-wrapper .auth-inner {
  width: 100%;
  position: relative;
}
</style>