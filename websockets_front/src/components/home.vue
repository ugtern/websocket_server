<template>
  <div>
    <button @click="change_button_text()" class="main_click reg_auth_checker" v-text="text"></button>
    <div v-if="auth_false===false">
      <input type="text" v-model="login">
      <input type="password" v-model="password">
      <button @click="reg" class="main_click" v-text="reg_button_text"></button>
    </div>
    <div v-if="auth_false===true">
      <input type="text" v-model="login">
      <input type="password" v-model="password">
      <button @click="authoriz" class="main_click" v-text="auth_button_text"></button>
    </div>
    <div class="chat_field">
        <div class="message_field" v-for="i in chat_messages">
          <span v-text="i" class="message_field"></span>
        </div>
    </div>
    <input type="text" v-model="message">
    <button @click="send_message()" class="main_click">Отправить</button>

  </div>
</template>

<script>
    export default {
        name: "home",
        data() {
            return {
                login: '',
                password: '',
                auth_false: false,
                auth_button_text: 'Авторизация',
                reg_button_text: 'Регистрация',
                text: 'Регистрация',
                message: '',
                chat_messages: ['fsda', 'asdg'],
                socket: ''
            }
        },
        methods: {
            authoriz() {
                $.ajax({
                    url: 'http://0.0.0.0:8090/auth/',
                    type: 'POST',
                    data: JSON.stringify({
                        login: this.login,
                        password: this.password,
                    }),
                    dataType: 'json',
                    success: (response) => {
                        sessionStorage.setItem('token', response.token);
                        this.socket = new WebSocket('ws://localhost:8765');
                    },
                    error: (response) => {
                        alert('Ошибка')
                    }
                })
            },
            reg() {
                $.ajax({
                    url: 'http://0.0.0.0:8090/reg/',
                    type: 'POST',
                    data: JSON.stringify({
                        login: this.login,
                        password: this.password,
                    }),
                    dataType: 'json',
                    success: (responce) => {
                        console.log('complete')
                    },
                    error: (responce) => {
                        console.log('error')
                    },
                })
            },
            send_message() {
                // socket.onopen = function () {
                //     alert('connected')
                // };
                // socket.onclose = function () {
                //     alert('closed')
                // };
                // socket.onmessage = function (event) {
                //     alert(event.data)
                // };
                let that = this;
                that.socket.send(this.message);
                that.socket.onmessage = function (m) {
                    let msg = m.data;
                    that.chat_messages.push(msg)
                }
            },
            change_button_text() {
              this.auth_false=!this.auth_false;
              if (this.auth_false === true)
                this.text = this.auth_button_text;
              else
                this.text = this.reg_button_text;
            }
        }
    }
</script>

<style scoped>
  .main_click {
    height: 40px;
    width: 240px;
    background-color: #2c3e50;
    color: white;
    border-radius: 8px;
  }
  .reg_auth_checker {
    background-color: #42b983;
  }
  .chat_field {
    background-color: antiquewhite;
    display: flex;
    border-style: inset;
    border-radius: 36px;
    height: 350px;
    flex-direction: column;
  }
  .message_field {
    display: flex;
  }

</style>
