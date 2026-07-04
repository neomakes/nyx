# Nyx

Nyx는 GPS, 통신, 클라우드 접근, 현장 확신이 동시에 약해지는 상황에서
대원이 방향감과 판단 기준을 잃지 않도록 돕는 **로컬 우선 해커톤 데모**입니다.

Nyx는 전술 지휘 체계가 아닙니다. 사람, 위협, 무기, 위험물, 진입 가능 여부를
식별하거나 확정하지 않습니다. 이 레포가 보여주는 것은 하나의 인터페이스
패턴입니다.

```text
약한 증거 -> 보수적 상태 판단 -> 짧은 행동 카드 -> 사람의 최종 판단
```

## 왜 만들었나

실내, 지하, 참호, 통신 두절 공간에서는 “내 위치가 어디인가?”만으로는 부족합니다.
더 중요한 질문은 보통 이것입니다.

```text
지금도 경로, 마지막 체크포인트, 임무 의도를 믿을 수 있는가?
```

Nyx는 긴 답변 대신 작은 드릴 카드로 답합니다.

| 상태 | 뜻 | 기본 방향 |
|---|---|---|
| `RE-ORIENT` | 마지막으로 믿을 수 있는 기준점이 낡았거나 사라짐 | 체크포인트 회복 |
| `REALIGN` | 경로와 관찰된 랜드마크가 어긋남 | 서로 다른 단서 2개로 재정렬 |
| `HOLD` | 증거가 약해서 확신을 올릴 수 없음 | 과잉 확정 금지 |
| `HANDOFF` | 다른 자산이나 팀 확인이 필요함 | 표시, 기록, 인계 |

## 왜 중요한 문제인가

지하와 통신 두절 환경은 예외 상황이 아닙니다. 과거와 현재의 전장에서 반복되는
문제입니다. 지도는 불완전하고, 대원은 압박을 받으며, 가장 위험한 실수는
약한 증거를 강한 확신으로 바꾸는 것입니다.

| 패턴 | 보여주는 것 | Nyx가 번역한 문제 |
|---|---|---|
| 베트남전 터널 체계 | 지하 터널망은 지상 감시와 화력 우세를 약화시키고, 소규모 인원을 어둡고 좁은 저맥락 공간으로 밀어 넣었습니다. | 똑똑한 답변보다 먼저 방향감과 기준점을 지켜야 합니다. |
| 한반도 땅굴 위협 | 북한의 땅굴 활동은 SubT 문제가 한국 안보에서 추상적 미래가 아니라 실제 경험된 문제임을 보여줍니다. | 지하 경로 신뢰도를 별도 상태로 다룹니다. |
| 우크라이나 참호전과 전자전 | 참호선, 드론, 재밍, 통신 저하는 GPS와 원격 확신이 얼마나 빨리 깨질 수 있는지 보여줍니다. | 로컬 카드만으로도 정지, 재정렬, 인계 판단을 도와야 합니다. |

핵심 문장은 단순합니다.

```text
환경이 신호를 부정할 때, 시스템은 확신을 지어내면 안 된다.
```

Nyx가 집중하는 순간은 나쁜 결심이 내려지기 직전입니다.

```text
마지막 체크포인트가 오래됨
관찰된 랜드마크가 애매함
접촉 또는 경로 증거가 약함
대원이 계속 가도 되는지 묻는 상황
```

좋은 데모 행동은 절제입니다.

```text
RE-ORIENT. REALIGN. HOLD. HANDOFF.
```

## 레포 구조

```text
.
├── app.py
├── demo/
│   ├── index.html
│   └── sample_scenarios/
├── docs/
│   ├── claim_boundary.md
│   ├── demo_story.md
│   ├── judging_notes.md
│   └── problem.md
└── src/
    └── nyx_demo/
```

이 데모는 의도적으로 작습니다. 공개 레포에는 발표와 심사용 stub만 있습니다.
제품용 센서 스택, 운용 규칙 엔진, 내부 구현 자산은 포함하지 않습니다.

## 실행

```bash
python3 app.py
```

브라우저에서 엽니다.

```text
http://localhost:8080
```

다른 포트를 쓰려면:

```bash
NYX_PORT=18080 python3 app.py
```

## 확인할 것

1. 헤더에 `Nyx`가 보입니다.
2. 왼쪽 패널에서 signal-denied drill 상태를 고를 수 있습니다.
3. Action Card는 경로, 사람, 위험, 진입 가능 여부를 과잉 확정하지 않습니다.
4. 출력은 압박 상황에서도 읽을 수 있을 만큼 짧습니다.

## 경계

Nyx는 보수적 인터페이스 패턴을 보여주는 해커톤 데모입니다.

Nyx는 다음이 아닙니다.

- 실전 배치 장비
- 군사 조언
- 표적화 소프트웨어
- 자율 통제 시스템
- 안전 인증된 판단 체계
- 사람, 위협, 위험물, 무기 식별기
- 진입 허가 또는 작전 명령 생성기

## 공개 참고 자료

아래 링크는 문제 유형을 설명하기 위한 공개 자료입니다. Nyx는 이 자료의 전술,
절차, 세부 운용법을 구현하지 않습니다.

- [Underground Warfare 101 - Modern War Institute, West Point](https://mwi.westpoint.edu/underground-warfare-101/)
- [Subterranean Operations: Israeli Defense Force Lessons from Gaza - U.S. Army](https://www.army.mil/article/288356/subterranean_operations_israeli_defense_force_lessons_from_gaza)
- [Củ Chi tunnels - Wikipedia](https://en.wikipedia.org/wiki/C%E1%BB%A7_Chi_tunnels)
- [Third Tunnel of Aggression - Wikipedia](https://en.wikipedia.org/wiki/Third_Tunnel_of_Aggression)
- [In Ukraine's trenches, the warfare is electronic - Le Monde](https://www.lemonde.fr/en/international/article/2024/05/24/in-ukraine-s-trenches-the-warfare-is-electronic_6672587_4.html)
