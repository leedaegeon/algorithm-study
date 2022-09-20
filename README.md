# algorithm-study# algorithm-study

<body>
  <h1>
brute force approach
  </h1>
    <b>
•	정의
    </b>
  <ul>
  o 구하기 위해서 가능한 모든 솔루션을 탐색하는 접근 방식이다(가장 기본이 되고 간단한 접근 방법이다.)
  </ul>
  <b>
•	복잡도
  </b>
  <ul>
  o	O(m*n)
  </ul>
  <b>
•	Brute force approach가 필요한 경우
  </b>
  <ul>
  o	문제를 풀기위한 다른 접근방식이 성능개선이 불가할 때
  
  
    Ex) 사전에서 특정 단어를 찾을 때brute force접근법은 시간 복잡도가 O(n)이지만 binary search(전체 사전을 반으로 나누어 각 포션별로 탐색)를 사용하면  O(logn)이 된다. 만약 사전이 정렬   되어 있지 않다면 brute force를 적용해야 한다.
      
  o	가능한 답을 모두 찾아야 할 때
  </ul>
  <b>
•	장점
  </b>
<ul>
  o	가능한 모든 답을 찾으며, 적절한 문제의 답을 보장한다.
  
  o	많은 문제에 적용할 수 있다.
  
  o	간단한 문제를 해결하는데 사용된다.
  
  o	It can be considered a comparison benchmark to solve a simple problem and does not require any particular domain knowledge.
  
  o	 비교기준으로 사용되며 도메인에 대한 정보가 필요 없다.
  </ul>
  <b>
•	단점
  </b>
  <ul>
  o	가능한 모든 경우를 탐색 해야 하기 때문에 비효율적이다.
  
  o	해를 구할 수 있는지, 없는지 고려가 우선 되어야 한다.
  
  o	다른 알고리즘과 비교할 때 창의적이고 생산적인 결과를 갖지 못한다.
  </ul>
  <b>
•	예시
  </b>
  <ul>
  o	N자리 비밀번호를 갖는 자물쇠를 푸는 문제
  
    0000~9999까지 모두 시도해봐야 한다.
      
  o	정렬되지 않은 사전에서 특정 단어를 찾고자 할 때
  
    사전을 반으로 갈라도 정렬되어 있지 않아 모두 탐색해야 한다.
      
  o	약수의 합 구하기
  
    특정 수n의 약수를 구할 때  k<=n인 모든 k로 n을 나누어 봐야 한다.
  </ul>
  <b>
•	반복하는 횟수 계산
    </b>
    <ul>
  o	1억번의 연산 처리에 1초 소요
  
  o	만약 한 for문당 반복횟수(n)가 100이라면 3중 for문에서는 반복 횟수가 1,000,000번
  
  o	문제풀기 전에 시간제한에 걸리지 않는지 확인 가능
  
  o	입력 받은 데이터를 굳이 정제할 필요 없다. 최대한 입력 받은 대로 사용
    </ul>
  <h1>
recursive algorithm
</h1>
<b>
•	정의
</b>
<ul>
  o 재귀알고리즘은 자기 자신을 호출하는 알고리즘이다. 재귀 시 더 작은 입력값을 가지며 그 값에 대한 결과를 반환한다.
</ul>
<b>
•	사용할 때
 </b>
 <ul>
  o 어떤 문제가 자신의 더 작은 버전의 솔루션을 통해 해결되며 더 작은 버전이 해결가능한 문제로 작아질 수 있을 때 적용
  </ul>
  <b>
  •	구현
  </b>
  <ul>
  o재귀 알고리즘을 구현할 때 주어진 문제를 두 파트로 나눈다.
    <ol class = "a">
    <li>base case</li>
     base case란 이 보다 간단한 솔루션이 없는 상태, 재귀를 끝낼 수 있는 상태이다.
    <li>recursive step</li>
     recursive step이란 더 작은 입력값을 갖는 재귀함수를 호출함으로써 결과를 계산한다.
    </ol>

  </ul> 
<h1>
 Breadth-first Search(Graph1)
    </h1>
    <b>
•	카테고리
    </b>
  <ul>
o	Graph search->Uninformed Serch Strategies->Breadth-first Search
    <br>
Uninformed는 init부터 goal까지 path  cost정보가 없는 상태
   </ul>
 <b>
•	What is problem solving?
 </b>
<br>
    <ul>
   o State space에서 최초상태에서 목적상태까지의 sequence of operator(path)를 search하는 것(solution은 path or goal state)
    </ul>
<b>
•	목적
</b>
 <br>
    <ul>
     o Problem solving의 최종 목적은 경로 비용의 최소화
    </ul>
<br>
<b>
•	Formalize(informal problem description->formal…)
</b>
 <br>
    
o	정의해야 하는 것들
    <ol>
      <li>	Initial state</li>
      <li>	Operators</li>
      <li>	Goal test</li>
      <li>	Path cost function</li>
        >	input search algorithm
    </ol>
Initial state, operators정의는 state space를 구성한다.
    <br>
    
  <b>
  예시(8-puzzle)
    </b>
    <ol>
      <li>	States</li>
    	아홉개로 나뉘어진 네모칸에 있는 8개의 타일 위치
      <li>	Operators(successor function)</li>
    	빈칸을 상하좌우로 움직이기
      <li>	Goal test</li>
     	State matches the goal configuration
      <li>	Path cost</li>
    	각 스텝당 1

    
    
</body>

