function searchTerm(term) {
    // 데이터를 POST로 전송하려면 객체를 생성해야 합니다.
    const data = {
      session: "firstagent-huvu", // 세션 ID 설정
      queryInput: {
        text: {
          text: term, // 사용자가 입력한 검색어
          languageCode: "ko" // 언어 코드 설정
        }
      }
    };
  
    // fetch 함수를 사용하여 서버에 POST 요청을 보냅니다.
    fetch('http://13.125.127.220:3000/webhook', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(responseData => {
      // responseData 객체에는 서버에서 반환된 JSON 데이터가 포함되어 있습니다.
      // 여기에서는 단순히 응답 텍스트를 콘솔에 출력하고 있지만,
      // 웹 페이지에 결과를 표시하도록 코드를 추가할 수 있습니다.
      console.log(responseData.fulfillmentText);
    });
  }
  
  // 특정 용어에 대한 검색을 실행합니다.
  searchTerm("간극");
  