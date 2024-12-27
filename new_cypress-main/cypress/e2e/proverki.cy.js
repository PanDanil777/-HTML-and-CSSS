describe('Проверка авторизации', function () {

    it('Верный пароль и верный логин', function () {
         cy.visit('https://login.qa.studio/');
         cy.get('#mail').type ('german@dolnikov.ru');
         cy.get('#pass').type ('iLoveqastudio1');
         cy.get('#loginButton').click(); //нашел кнопку Войти и нажал на неё
         cy.get('#exitMessageButton > .exitIcon').should('be.visible'); // проверил есть ли кнопка крестик и она видна пользователю

    })  

    it('Верный логин и неверный парль', function () {
        cy.visit('https://login.qa.studio/');
        cy.get('#mail').type ('german@dolnikov.ru');//ВВели верные данные
        cy.get('#pass').type ('iLoveqastudio7');//ВВели НЕверные данные
        cy.get('#loginButton').click(); //нашел кнопку Войти и нажал на неё
        cy.get('#messageHeader').contains('Такого логина или пароля нет');// текст совпадает
        cy.get('#exitMessageButton > .exitIcon').should('be.visible'); // проверил есть ли кнопка крестик и она видна пользователю

   })  

   it('НЕВЕРНЫЙ логин и верный парль', function () {
    cy.visit('https://login.qa.studio/');
    cy.get('#mail').type ('german@dolnikovм.ru');//ВВели НЕверные данные
    cy.get('#pass').type ('iLoveqastudio7');//ВВели верные данные
    cy.get('#loginButton').click(); //нашел кнопку Войти и нажал на неё
    //cy.get('#messageHeader').contains('Такого логина или пароля нет');// текст совпадает
    cy.get('#exitMessageButton > .exitIcon').should('be.visible'); // проверил есть ли кнопка крестик и она видна пользователю

}) 

   it('Ошибка валидации', function () {
    cy.visit('https://login.qa.studio/');
    cy.get('#mail').type ('germandolniko.ru');//ВВели НЕерные данные
    cy.get('#pass').type ('iLoveqastudio1');//ВВели верные данные
    cy.get('#loginButton').click(); //нашел кнопку Войти и нажал на неё
    cy.get('#messageHeader').contains('Нужно исправить проблему валидации');// текст совпадает
    cy.get('#exitMessageButton > .exitIcon').should('be.visible'); // проверил есть ли кнопка крестик и она видна пользователю

}) 
   it('Ошибка валидации', function () {
    cy.visit('https://login.qa.studio/');
    cy.get('#mail').type ('GerMan@Dolnikov.ru');//ВВели НЕерные данные
    cy.get('#pass').type ('iLoveqastudio1');//ВВели верные данные
    cy.get('#loginButton').click(); //нашел кнопку Войти и нажал на неё
    cy.get('#messageHeader').contains('Авторизация прошла успешно');// текст совпадает
    cy.get('#exitMessageButton > .exitIcon').should('be.visible'); // проверил есть ли кнопка крестик и она видна пользователю

}) 

 })

 

 /*describe('Проверка авторизации', function () {

    it('Верный пароль и верный логин', function () {
         cy.visit('https://login.qa.studio/');
         cy.get('#forgotEmailButton').click(); //нашел кнопку Войти и нажал на неё
         cy.get('#mailForgot').type ('german@dolnikov.ru');
         cy.get('#exitRestoreButton > .exitIcon').should('be.visible')
         cy.get('#exitRestoreButton > .exitIcon').click();
         //cy.get('#messageHeader').contains('Успешно отправили пароль на e-mail');
         //cy.get('#messageHeader').should('be.visible');
        // cy.get('#exitRestoreButton > .exitIcon').should('be.visible'); // проверил есть ли кнопка крестик и она видна пользователю

    })  
 })*/