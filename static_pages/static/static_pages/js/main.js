let advice = (title, date, desc, author) => ({title, date, desc, author});

let myAdvice = [
   advice(
      'Frontend разработка',
      '19/07/2018',
      'Работаю Frontend разработчиком 3 года в такой то такой компаний и много много текста'
   ),
   advice(
      'Пару слов о Backend',
      '15/04/2018',
      'Работал Backend разработчиком 2 года, могу дать простые советы'
   ),
   advice(
      'Web Design',
      '04/01/2018',
      'Фрилансил веб дизайнеров несколько месяцев, поделюсь рекомендациями по фотошопу и посторению UX/UI'
   ),
   advice(
      'Web Design',
      '04/01/2018',
      'Фрилансил веб дизайнеров несколько месяцев, поделюсь рекомендациями по фотошопу и посторению UX/UI'
   ),
];

let otherAdvice = [
   advice(
      'Machine learning',
      '14/11/2017',
      'Опыт работы в ML 4 года',
      'Erkebulan Duisebay'
   ),
];


var  COUNTER = 2;

function removeDesc(id) {
   console.log('delete')
   let deleteElement = document.getElementById('how-learn-box');
   console.log(deleteElement.children[id])
   deleteElement.removeChild(deleteElement.children[id])
   COUNTER--;
   let HIDDEN_COUNTER = document.getElementById('id_form-TOTAL_FORMS'); 
   HIDDEN_COUNTER.value = COUNTER
}

function addDesc() {
    console.log("---------=============")
    console.log(COUNTER)


   let mainBox = document.getElementById('how-learn-box');
   let howToLearnBox = document.createElement('div');
   let createDeleteBox = document.createElement('div');
   let createDelete = document.createElement('i');
   let createInputBox = document.createElement('div');
   let createInput = document.createElement('input');
   let linkInput = document.createElement('input');
   let hr = document.createElement('hr')

   howToLearnBox.className = 'how-to-learn';
   createDeleteBox.className = 'how-to-learn__delete';
   createDelete.setAttribute('aria-hidden', 'true');
   createDelete.setAttribute('onclick', 'removeDesc('+ COUNTER +')');
   createDelete.title = 'Удалить поле';
   createDelete.className = 'fa fa-minus-circle';
   createInputBox.className = 'how-to-learn__add';

   createInput.type = 'text';
   createInput.className = 'input-text';
   createInput.placeholder = 'Краткое описание';
   createInput.name = 'form-'+ COUNTER +'-description'

   linkInput.type = 'text';
   linkInput.className = 'input-text';
   linkInput.placeholder = 'Cсылка на материал';
   linkInput.name = 'form-'+ COUNTER +'-link'

   let addMainBox = mainBox.appendChild(howToLearnBox);
   let addCreateDeleteBox = addMainBox.appendChild(createDeleteBox);
   let addCreateInputBox = addMainBox.appendChild(createInputBox);

   addCreateDeleteBox.appendChild(createDelete);
   addCreateInputBox.appendChild(createInput);
   addCreateInputBox.appendChild(hr);
   addCreateInputBox.appendChild(linkInput);
   addCreateInputBox.appendChild(hr);
   addCreateInputBox.appendChild(hr);

   COUNTER ++;
   let HIDDEN_COUNTER = document.getElementById('id_form-TOTAL_FORMS'); 
   HIDDEN_COUNTER.value = COUNTER
};

new Vue({
   el: '#app',
   delimiters: ['[[', ']]'],
   data: {
      tabs: ['Мои рекомендации', 'Сохраненные рекомендации'],
      myAdvice: myAdvice,
      otherAdvice: otherAdvice,
      currentTab: 0,
      stepsList: false,
      skills: [
         'HTML5',
         'CSS3',
         'JavaScript',
         'jQuery',
         'VueJS',
         'Git',
         'Webpack',
         'SASS',
         'Gulp',
         'npm',
      ]
   }
});