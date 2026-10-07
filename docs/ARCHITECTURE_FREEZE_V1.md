# EVIDENCE INDEPENDENCE MATRIX — ARCHITECTURE FREEZE V1

日期：2026-10-06（Asia/Shanghai）  
阶段：Architecture Freeze，仅设计；未实现、未测试、未部署、未提交。  
规范版本：`EIM-V1-STUDIO`  
Primitive：Evidence Independence Matrix（EIM）  
Product：EchoMap  
Project 主标签：开发者工具  
本文件为下一阶段交接的架构依据，不是执行指令或 WORK HANDOFF PACKAGE。

## 0. 冻结前纠正与信任边界

### 0.1 不把依赖关系当作等价关系

方向研究中的“依赖图连通分量 = 独立证据族数量”不能成立。例如，A 使用数据 X，B 同时使用 X 和 Y，C 使用 Y；A–B、B–C 依赖，并不意味着 A–C 依赖。共享部分信息源的关系不具有传递性。

V1 因此冻结为：逐对判断、保留未知、计算最大两两独立集合。不得用 union-find、依赖图连通分量、不同域名数、没有引用链接等方法，声称已经得到真实独立证据总数。

`max_supported_independent_set_size` 只表达：在本次可见材料及共识矩阵中，最大的、任意两项之间均有 INDEPENDENT 关系的来源集合规模。它不是现实世界真实独立来源总数，也不是 claim 正确概率。

### 0.2 评估范围

本合约判断特定 claim 对应的可见证据来源关系，不判断 claim 真伪、不打来源信誉分、不认证发布者身份、不证明网页中的来源声明真实、不证明不存在隐藏共同来源。

INDEPENDENT 的完整含义是“可见材料中有积极证据支持相互独立的 claim 相关信息取得路径”。DEPENDENT 的含义是“可见材料中有积极证据支持共享或派生的 claim 相关信息来源”。证据不足必须 UNKNOWN。

共识提供的是按公开规则、由网络验证的共享解释结果；不能消除材料造假、验证者相关偏差、托管测试网信任或未来网页失效。

## A. Intelligent Contract Track

### A1. Primitive Name / Definition / Problem

**名称：Evidence Independence Matrix。**

**一句话定义：**对同一明确主张的 2–4 份公开材料，由 GenLayer 独立执行来源关系判断，生成不可修改的逐对独立性矩阵，供其他应用引用与确定性计算。

**底层问题：**多个链接可能重复同一份原始证据；链接数、域名数、作者数不能直接充当独立证据数。不同参与方也不应由其中一方的服务器私下决定材料是否独立。

**Why GenLayer：**来源关系包含引用、改写、共同数据、第一手取得路径等语义信息，不能仅靠哈希或固定字符串判断。GenLayer 把证据读取、独立语义判断、协议共识和持久化结果放在同一可核验流程中。

**Why Multi-Validator：**Leader 的误读、单方解释或恶意结论，需要其他参与者重新读取材料并独立判断，而不是只检查格式。没有这一过程，核心产物只剩一个服务商的分类答案。

服务器或 ChatGPT 能计算类似矩阵；本机制的区别是结果提交到网络的验证与状态流程，调用者不能在不改动合约/网络信任假设的情况下私自改写已有记录。Studionet 是托管开发环境，不能把演示的多验证者执行夸称为主网级、完全独立的组织/模型安全保证。

### A2. 可脱离 EchoMap 的复用场景

| 场景 | 其他开发者如何使用 |
|---|---|
| DAO 提案材料预检 | 自己提交 claim 和材料 URL，读取矩阵，标出重复来源 |
| 研究/尽调工具 | 读取最大两两独立集合，为用户提供材料选择建议 |
| 证据包 SDK / AI 工作流 | 使用固定 schema 消费矩阵；UNKNOWN 不自动满足独立证据门槛 |
| 其他 GenLayer 应用 | 通过兼容的 SDK 或 Intelligent Contract 调用读取记录，并自行设定业务阈值 |
| 教学 | 独立学习自定义验证者、未知分类、幂等、原子写入和非传递关系 |

A 仓库无前端依赖、无 EchoMap 品牌字段、无特定案例硬编码、无 Project 钱包白名单。复用不要求安装或打开 EchoMap。链间/EVM 桥接不属于 V1，也不宣称支持所有 EVM 合约直接调用。

### A3. 冻结的分类规则

输入必须是一条可讨论的、范围清楚的 claim；context 只能澄清地点、时间、术语或材料范围，不能改变合约规则。V1 的 provenance 指 claim 相关事实、观察、数据或规范信息的取得来源，不是页面域名或 HTML 文件作者。

RELEVANT 表示材料对这个 claim 提供实质相关的信息或取得路径，不要求其赞同 claim；NOT_RELEVANT 表示只有背景/关键词或与指定范围无关；UNCERTAIN 表示范围或关联无法确定。因此最大独立集合包含的是相关来源，不是“支持该主张的独立票数”。报告不得说“两个独立来源已经证实主张”。

| Relation | 必须满足 | 不能据此判定 |
|---|---|---|
| DEPENDENT | 明确的 claim 相关引用/派生关系，或共同的、可识别的原始数据/观察/规范来源 | 同一事件、同一立场、措辞相似、同一网站、普通背景引用 |
| INDEPENDENT | 两边均提供 claim 相关材料；可见材料积极描述不同、可区分的信息取得路径；没有可见的 claim 相关共同/派生来源 | 域名不同、作者不同、未发现链接、两边自称独立但无取得路径 |
| UNKNOWN | 无法依据上述规则建立关系；任一边不可读、不相关、相关性不明确，或 provenance 不足 | 不得当作 INDEPENDENT 或低可信度 DEPENDENT |

重要细则：

1. 判断范围必须绑定 claim。A 引用 B 的背景介绍，但 claim 依据自身调查，不自动 DEPENDENT。
2. 两边明确共享 claim 相关的实质证据，即使还各有其他材料，该 pair 仍 DEPENDENT。
3. 一个页面包含多个来源但无法辨清哪些支持 claim，该 pair UNKNOWN。
4. 一致结论不等于共同来源；两个独立采集的观测也可能针对同一个事件。
5. 完全相同文本在不同 URL 出现，若没有足够 provenance，不能仅凭哈希证明真实派生关系；仍按语义规则判断，必要时 UNKNOWN。
6. 不把“任何一个引用”视为依赖；也不把信息缺失当作独立的证据。
7. 对复合、含糊或不适合评估的 claim，不猜测业务意图。相关性可以 UNCERTAIN，进而保留 UNKNOWN。
8. 三种关系对称；不输出派生方向，不进行传递闭包。

### A4. State Schema

只有一张持久化映射：`assessments[request_id] -> Assessment`。包含三个核心记录结构：Assessment、SourceObservation、PairDecision。没有用户表、计分表、余额表、可变任务队列或历史版本树。

**Assessment：**

| 字段 | 定义 |
|---|---|
| protocol_version | 固定 EIM-V1-STUDIO |
| request_id | SHA-256 标识；算法见 A6 |
| creator | 实际合约调用者，规范化地址 |
| client_key | 调用者命名空间内的幂等键 |
| payload_digest | 规范化输入的 SHA-256 |
| claim / context | 规范化后的原始输入 |
| urls | 规范化、排序后的 2–4 个 URL |
| sources | 与 urls 同序的 SourceObservation |
| pairs | 按 i、j 升序排列的全部 PairDecision，i < j |
| result_status | COMPLETE 或 PARTIAL，确定性推导 |
| max_supported_independent_set | 最大两两独立集合的来源索引数组 |
| max_supported_independent_set_size | 上述数组长度 |
| dependent_pair_count / independent_pair_count / unknown_pair_count | 确定性计数 |

**SourceObservation：**

| 字段 | 定义 |
|---|---|
| index / url | 固定输入索引和 URL，非模型自由生成 |
| read_status | READABLE / UNAVAILABLE / UNSUPPORTED |
| content_digest | READABLE 时为规范化分析文本的 SHA-256；否则 null |
| relevance | RELEVANT / NOT_RELEVANT / UNCERTAIN / NOT_APPLICABLE |

**PairDecision：**仅 `i`、`j`、`relation`。不存自由文本解释、置信分、长篇推理或整页内容。解释区由前端使用固定规则文案及原始来源链接，展示该 enum 的含义；不得伪称为模型给出的详细理由。

创建时间、原始 transaction hash、多验证者数量等不在业务状态中伪造，由真实网络记录/提交证据关联。没有可靠 SDK 上下文字段时，不编造时间或交易哈希。

### A5. State Invariants

1. 记录只能完整写入一次，随后不可修改、删除或覆写。
2. 一个 request_id 只对应一个 creator、client_key 和 payload_digest。
3. SourceObservation 个数等于 URL 个数，索引为 0 到 n−1。
4. PairDecision 数等于 n(n−1)/2，每对出现一次；对角线不存储。
5. READABLE 必须有合法 digest；其他 read_status 的 digest 为 null、relevance 为 NOT_APPLICABLE。
6. 任一边不是 READABLE + RELEVANT 时，该 pair 必须 UNKNOWN；候选输出违反时拒绝，而不是偷偷改成 UNKNOWN。
7. 计数总和等于 pair 数；派生集合中的来源均为 READABLE + RELEVANT。
8. 集合内任意不同两项的 relation 均为 INDEPENDENT。
9. 未知不参与独立边构造；DEPENDENT 不作传递闭包。
10. 没有 UNKNOWN pair 时 result_status 为 COMPLETE，否则 PARTIAL。COMPLETE 只表示所有 pair 均分类，不表示 claim 被证实。
11. 没有任何合格来源时，集合为空、size 为 0；有合格来源但没有独立边时，size 可为 1，必须明确未确认任何独立来源对。
12. 合约记录存在不等于原始创建交易已经 FINALIZED；业务结果状态与网络交易状态分离。

### A6. Public Methods / Inputs / Outputs / Authorization

共 4 个 public methods：1 write + 3 view；部署构造器不另算业务方法。

| Method | Inputs | Outputs | Authorization |
|---|---|---|---|
| assess | client_key、claim、context、urls | request_id、disposition=NEW/REUSED、result_status | 任意调用者可提交；键归实际 sender 命名空间；不收业务款项 |
| get_assessment | request_id | found=false，或 found=true + 完整 Assessment | 公开只读，无钱包签名 |
| lookup_request | creator、client_key | request_id、found、已存在时 payload_digest/result_status | 公开只读，仅计算并查已有结果 |
| get_protocol_info | 无 | version、schema version、关系规则标识、输入限制、支持来源规则 | 公开只读 |

assess 返回值属于交易执行返回，前端必须从匹配版本的 SDK receipt/trace 适配获取；返回 request_id 不等于 finality。request_id 也可预先确定性计算，避免依赖一份暂时不可读的交易返回。

**输入限制：**

- client_key：1–64 个 ASCII 字符，限定字母、数字、下划线、连字符。前端一次新请求生成随机键并在签名前保存。
- claim：去首尾空白后 1–600 个 Unicode code points。
- context：去首尾空白后 0–400 个 Unicode code points。
- urls：2–4 个，规范化后每个不超过 512 UTF-8 bytes。
- creator：从合约调用上下文取得，用户不能指定 write 的 creator。

**规范化：**

- 文本：CRLF/CR 转 LF，去开头 BOM，去整体首尾空白；不合并内部空白、不改语言、大小写或标点。
- URL：只允许 ASCII HTTPS URL；scheme/host 转小写；省略默认 443；空路径视为 `/`；保留 path 大小写及转义形式。不允许 credentials、非 443 端口、query、fragment、反斜杠、控制字符、IP literal 或 dot path segments。
- 同一规范化 URL 重复直接拒绝，不静默删减来源。
- URL 按完整规范化字符串的 ASCII 字典序排序；索引据此确定。
- 哈希编码：UTF-8、无额外空格的规范 JSON 数组；地址为小写规范 hex；字符串保留 Unicode、不做转义风格随机变化。
- request_id = SHA-256([protocol_version, creator, client_key] 的上述编码)，对外用小写 64 位 hex，不附 `0x`。
- payload_digest = SHA-256([protocol_version, claim, context, sorted_urls] 的上述编码)。

view 输入非法格式返回明确输入错误；get_assessment 的合法但不存在 ID 返回 found=false，不误判成网络失败。

### A7. Duplicate Handling / Idempotency

| 情况 | 行为 |
|---|---|
| 同 creator + key + 相同规范化 payload，记录已存在 | 返回原 request_id、REUSED；不访问网页、不调用 LLM、不重算结果 |
| 同 creator + key，payload 不同 | IDEMPOTENCY_CONFLICT；不写任何状态 |
| 同 payload，新 key | 允许新观察，NEW；旧记录保持不变 |
| 不同 creator，同 key | 独立命名空间，互不占用 |
| 失败/未达成共识，未产生记录 | 终态确认后可原 key 重试；未确认终态不自动重发 |
| 已存 PARTIAL，希望重新评估 | 新 key 发起新观察；原 key 仍 REUSED |

幂等保护的是“只创建一次业务记录”，不保证重复提交没有网络费用。前端先 lookup，尽量避免重复交易。并发提交依靠网络的合约执行排序和同键检查，不在合约中建立异步锁或 pending 记录。

### A8. State Transitions

只有业务级转换：ABSENT → IMMUTABLE_ASSESSMENT。COMPLETE/PARTIAL 是写入时推导的结果完整度。

流程：输入校验 → 幂等检查 → 建立纯内存输入 → nondeterministic consensus → 验证候选与 invariants → 确定性统计 → 一次原子保存 → 返回。

输入错误、模型故障、网络故障或无共识：不创建记录、不创建失败报告、不保存半张矩阵。网络 Pending/Accepted/Finalized/Undetermined 等状态不在合约字段中模拟；由网络决定。即便交易已经 FINALIZED，执行失败也不能显示成功。

### A9. Nondeterministic Execution

一条主要共识路径，采用稳定 GenLayer SDK 的 custom Leader/Validator mechanism，当前官方对应 `gl.vm.run_nondet_unsafe`。语法绑定时可适配，但独立判断和以下验证语义不得替换。

每次执行由每个参与者完成：

1. 独立取得每个输入 URL；不接受浏览器代取的正文作为正式证据。
2. 对可用正文按 A13 规范化并计算 digest。
3. 最多一次 LLM 调用，读取所有可用材料、claim 和 context，完整分类 source relevance 及所有 pairs。
4. 确定性解析、验证、压缩成 canonical candidate。

若没有任何可读材料，可不调用 LLM，直接形成全部 NOT_APPLICABLE / UNKNOWN 的合法候选。网络内部轮换可能让这个流程执行多轮；“一次 LLM”是每位参与者每次执行的目标，不是整笔交易必定只调用一次。

不在 nondeterministic block 中读写持久化状态；需要的输入先复制到内存。不存在逐 pair 各自启动共识或各调用一个 prompt 的设计。

### A10. Leader Responsibility

- 依据同一规则独立 fetch，计算观察摘要。
- 独立判断材料是否与 claim 有关，以及所有 pair 的来源关系。
- 不使用域名差异、文本相似度或来源数量代替语义判断。
- 输出完整 canonical candidate；不能把调用失败伪装成 UNKNOWN。
- 不写状态、不计算可信度、不输出业务裁决或 claim 真伪。

### A11. Validator Responsibility

- 明确验证 Leader 返回的是成功候选，不是错误/异常包装；异常不视为默认通过。
- 用自己的请求重新获取所有 URL，独立计算 digest 和完整分类；LLM prompt 不包含 Leader 的答案，避免诱导确认。
- 校验自己的候选和 Leader 候选均满足 schema、枚举、边界和 invariant。
- 对每个 source 和 pair 比较实质字段；任何实质差异返回 disagree。
- 控制并区分外部数据、模型和解析故障；无法独立验证就拒绝，不改成 accept。

不得只检查 JSON shape、非空、enum 合法或摘要好看。不得把 Validator 退化为“同意 Leader 的解释”。

### A12. Equivalence / Validation Principle 与 Canonical Output

**冻结原则：Evidence-Bound Pairwise Equivalence。**

Leader 和 Validator 的 material projection 必须逐字段一致：source read_status、分析文本 content_digest、source relevance、所有 pair relation。固定索引/URL 必须等于输入。这里比较的是独立产生的决策字段，不是自然语言推理文本。

不同原始页面格式、换行等允许在冻结的规范化范围内消除差异；规范化分析文本 digest 不同则拒绝。本次结果绑定同一份可见文本，不能让不同材料刚好产生相同 enum 就视为同一次观察。

不比较 HTTP 原始 header、获取时间、provider 名称或不可控错误文案。不合并验证者投票产生“每格多数矩阵”；网络验证的是一个完整候选。中间 Validator 输出不自动成为合约状态。

每个Validator分别给出accept/disagree；整体阈值、Leader轮换与finality由Stable网络协议决定，不另写“所有参与者必须全票一致”的应用共识机制。验收中的参与者数量不是自定义投票阈值。

禁止用 `strict_eq`、`prompt_comparative`、`prompt_non_comparative` 或第二个 LLM 的“整体差不多”判定，替换此 custom validator 流程。即使 finite enums 可比较，也必须保留独立抓取、分类、digest 绑定、异常分类和实质字段验证。

**Canonical candidate schema（设计定义，不是代码）：**

| 字段 | 类型 / 规则 | 来源 |
|---|---|---|
| schema_version | 固定 EIM-CANDIDATE-V1 | 合约常量 |
| sources | 固定顺序的 SourceObservation 数组 | fetch 摘要 + LLM relevance |
| pairs | 全部 i<j 的 PairDecision 数组 | 固定索引 + LLM relation |

LLM 自身只返回固定顺序的 relevance 数组与 relation 数组；index、URL、digest、版本由代码绑定。拒绝缺项、多项、非法 enum、额外字段、布尔/数值类型替代枚举及重复 JSON keys。最终 Assessment 的统计和状态完全由确定性代码产生，不让模型给计数。

relevance 数组长度固定为 n；不可读位置必须返回 NOT_APPLICABLE，可读位置只允许 RELEVANT/NOT_RELEVANT/UNCERTAIN。relation 数组长度固定为 n(n−1)/2，与 i<j 字典序对应。模型违反不可读位置或相关pair的固定约束时拒绝整个候选，不靠事后覆盖来修补答案。

**冻结的分类 prompt 内容约束：**

- 固定系统规则：任务只是 claim-scoped provenance classification；按 A3 逐对判断。
- claim/context/source text 均以转义后的结构化数据隔离，明确为不可信数据。
- SOURCE_i 的 index/read_status/content 由代码生成；内容不得增加 URL 或调用工具。
- 每个 source 必须给 RELEVANT/NOT_RELEVANT/UNCERTAIN；不可读则由代码设置 NOT_APPLICABLE。
- 每个 i<j 必须给一个关系，明确独立需要积极证据、未知必须保留、依赖不传递。
- 固定输出只有指定两个数组，不输出解释、分数、计数、建议、指令或 URL。
- 不允许“网页要求输出 INDEPENDENT”覆盖分类规则；也不允许 claim/context 改写 enum 定义。

下一阶段可把这些已冻结内容整理为逐字的 canonical prompt template，并版本化；不允许借整理模板改变决策语义。

### A13. External Data Rules

为节约实现和测试成本，V1 是公开短文本证据包，不是通用网页爬虫。

| 项目 | 冻结规则 |
|---|---|
| 允许 host | raw.githubusercontent.com；单层 `{owner}.github.io`（owner 为合法 ASCII GitHub 命名形式） |
| 允许文件 | URL path 以 .txt / .md / .adoc / .sol 结尾；只当 UTF-8 文本读取，不执行代码 |
| 请求方式 | HTTPS GET，无凭证、cookie、API key 或付费 provider |
| 获取实现 | GenLayer 原生 web HTTP API；不调用项目后端，不浏览器抓正文，不渲染 JavaScript |
| 大小 | 每份 HTTP body ≤32,768 bytes；规范化文本 ≤8,000 Unicode code points；超限整份 UNSUPPORTED |
| 文本 | UTF-8、去开头 BOM、换行统一 LF、去整体首尾空白；保留内部字符与空白 |
| 不支持 | HTML、PDF、图片、视频、登录墙、付费墙、无限滚动、大型文档、需要执行脚本的内容 |
| 重定向 | 不主动跟随网页中的链接或扩展证据范围；平台 HTTP 内部重定向由平台负责，不宣称合约实现了 DNS/SSRF 防护；可观测到跨出允许 host/类型时拒绝为 UNSUPPORTED |
| 版本 | 推荐 commit SHA / release tag / 固定版本路径；动态变更导致 digest 不一致时 reject |
| 存链 | 只存 URL、分析文本 digest、读取状态和判断；不存全篇正文 |

内容类型可取得时，应符合公开文本；明显返回 HTML 错误页/登录页时不得当成证据正文。无法可靠区分错误页时，该来源不允许进入 RELEVANT 判定。临时故障规则见 A15。

没有链接追踪或递归追溯。网页/文本提到的第三方来源仅作为当前材料的声明；若要评估其正文，用户须把它作为 2–4 项输入之一。未实际获取的出处不得被说成已核验。

记录是一次可见文本的关系评估，digest 不是全文备份。网页后来变更/删除时，旧判断仍能读取，但不能保证重新恢复旧正文。官方或第三方原始文本不因被镜像到 GitHub 就变成独立来源。

### A14. Deterministic Post-processing

1. 验证所有 schema 和 invariant。
2. 构建对称矩阵；对角线仅在前端显示 SELF，不作为第四种关系存链。
3. 计数三种 pair；从 UNKNOWN 是否存在推导 COMPLETE/PARTIAL。
4. 选出 READABLE + RELEVANT 的候选来源。
5. 枚举候选来源的所有子集（n≤4，总计最多16个），只有任意不同两项均为 INDEPENDENT 才是合法独立集合。
6. 选最大规模；同规模按升序索引数组的字典序选择最小者。
7. 保存上述结果；前端可以重新算以核对，但不能覆盖链上结果或把 UNKNOWN 升级。

size=1 时显示“未确认任何来源对独立，可单独保留一个相关来源”；size=0 时显示“没有可用于该 claim 的相关可读来源”。不得显示“0/1 个真实独立证据族”。

### A15. Error Handling / Failure Modes

| 故障 | 处理 | State 影响 |
|---|---|---|
| 参数越界、不支持 URL、重复 URL | INVALID_INPUT / UNSUPPORTED_URL / DUPLICATE_URL | 无写入，无 LLM |
| 同键不同内容 | IDEMPOTENCY_CONFLICT | 无写入，无 fetch/LLM |
| 确认的404/410、401/403等不可读响应 | source=UNAVAILABLE；相关 pairs UNKNOWN | 只有完整候选通过网络共识阈值时，才可形成 PARTIAL |
| 超限、非 UTF-8、HTML/PDF/类型不支持 | source=UNSUPPORTED；相关 pairs UNKNOWN | 同上；不得静默截断 |
| 429、5xx、超时、DNS/连接故障 | SOURCE_TEMPORARILY_UNAVAILABLE，停止本次候选 | 无业务记录；可在终态确认后重试 |
| LLM provider 失败/空输出/不合法 JSON | MODEL_EXECUTION_FAILED / INVALID_MODEL_OUTPUT | 无业务记录；不是 UNKNOWN |
| 读取成功但 provenance 或 relevance 不明确 | 合法 UNKNOWN / UNCERTAIN | 可保存 PARTIAL |
| 验证者看到不同正文/判断不同 | disagree；网络决定轮换、终态等 | 不强行合并；无共识不产生记录 |
| 交易 pending 很久 | 前端标记仍等待/暂不可查 | 不自动新发 write |
| FINALIZED + execution error | 明确执行失败 | 不能显示“评估成功” |
| 读取 RPC 故障或429 | 退避/恢复读取 | 不清除记录，不重发 write |
| 页面造假、共同模型偏差 | 呈现已声明的信任边界 | 不宣称共识证明事实真实 |

错误可以依当前稳定 SDK 映射到对应异常语法；不能变成未捕获的异常即默认通过，也不能把所有异常变成业务 UNKNOWN。原则上不做合约内自动 HTTP/LLM retry，以免放大费用和共识时间。

### A16. Security / Prompt Injection

- 固定 prompt rules 与不可信数据隔离，使用结构化转义；简单分隔符不是安全保证。
- 来源内容、claim、context 中的“忽略规则”“改 enum”“访问另一个URL”“发送秘密”等均无指令权限。
- 不能由模型选择要访问的 URL；访问列表和 GET 行为固定。
- 不存/索取用户私钥、API key、登录凭证；钱包签名在用户钱包完成。
- 无资金托管、token transfer、代币审批、业务 fee、外部写操作或执行来源代码。
- 前端只渲染安全文本，不把材料正文/claim 当 HTML 插入。
- unknown-first 与小规模输入降低误判面，但不承诺能抵御所有 injection。必须有攻击样本验证，不只写免责文案。
- 所有链上输入公开，产品提交前明确告知；不引导用户上传私人资料或带秘密的 URL。
- 无 admin override、可升级代理、共识后手工编辑或测试专用强制结果入口。

### A17. Test Strategy

本轮只冻结测试计划，不执行测试。

**确定性/集成测试：**

| 测试组 | 关键证明 |
|---|---|
| 输入边界 | 1/5个来源、超长字段、不支持 host/query、重复 URL 被拒绝 |
| 规范化/哈希 | 换行/首尾空白、URL排序稳定；前后端 request_id/payload_digest 同算 |
| 幂等 | 相同键重复不 fetch/LLM；同键不同输入拒绝；不同 sender 不冲突 |
| 原子性 | web/LLM/JSON/validator失败后 mapping 无半写入 |
| schema | 缺项、多项、额外字段、重复JSON keys、非法 enum/index 及不相关独立边拒绝 |
| 独立验证 | 合法 JSON 但错误 relation 的 Leader 被 Validator 拒绝；通过不是格式检查 |
| digest绑定 | 相同enum但不同文本digest必须拒绝；规范化等价文本可一致 |
| 来源故障 | 404/超限与429/超时按不同路径处理，不静默截断 |
| 非传递关系 | A–B=D，B–C=D，A–C=I 能合法保存；不得合并后改写A–C |
| 集合计算 | 全I、全D、全U、混合、无合格来源、单来源、并列tie-break |
| claim范围 | 仅背景引用不自动D；一致结论或不同host不自动I |
| prompt injection | 恶意“全I”正文不能覆盖规则；不得访问新增URL |

采用当前可用稳定测试工具/mock 来验证控制流；mock 结果不能当作真实 AI 共识已完成的证明。

**真实 Studionet 验证：**至少覆盖一份混合关系的受控样本和一份真实文档的共同来源样本；使用 Normal/full consensus 对应的稳定网络模式，目标5个、至少3个实际参与者（含Leader）。以 Explorer/receipt/节点信息证实实际参与数量与 FINALIZED + execution success。不能用前端固定文案或 mock 标签冒充多验证者。

如托管网络当前无法实现最低真实多参与者验收，记录阻塞并请求下一步决定，不切换其他测试网、不降低为单Leader、不提供付费provider作为默认解决办法。

### A18. Standalone Demo

不使用 EchoMap 即可完成：

1. 在 Studio 加载 A 仓库合约并部署到 Stable Studionet。
2. 按 A 仓库 examples/README 输入 claim、context、公开 fixture URL、client_key 调用 assess。
3. 在 Explorer 查看真实交易生命周期、多参与者证据及执行结果。
4. 调用 get_assessment，读取逐对关系和确定性集合。
5. 同键相同输入再次调用，得到 REUSED；说明不重新读取来源。

A 仓库自己提供短文本 fixtures、预期关系说明、输入示例、测试与部署说明；可将其托管到自己免费 GitHub Pages。不得依赖 B 仓库的网页、构建、配置或专有数据才能理解与测试。

### A19. Intelligent Contracts Submission Mapping

| 截图标准 | A 提交证明 |
|---|---|
| useful / reusable / educational | 通用schema、4个方法、至少3种复用方法、独立Studio示例 |
| real consensus logic | custom validator源代码、独立fetch+分类、错误Leader拒绝测试、真实multi-participant transaction |
| clear state design | 3种记录结构、invariants、原子写入、幂等说明 |
| thoughtful validators / equivalence | digest绑定与逐对relation/relevance比较，UNKNOWN规则及非传递性 |
| meaningful beyond one-off demo | 任意合规claim/evidence输入，非EchoMap专用模块 |
| readable source/docs/tests | 独立 README、协议说明、测试、部署清单、license、SDK版本 |
| 不属于薄LLM/简单storage | 完整共识检查、稳定输出、确定性集合、失败与重复语义，不存一个随意AI答案 |

提交A主URL为A仓库。合约地址、SDK/GenVM绑定版本、部署source commit、至少一笔真实共识交易及只读结果作为证据；B前端不是A成立的必要材料。

## B. Project Track

### B1. Product / Target User / Trust Problem

**名称：EchoMap。**

**一句话：**帮助研究者和 DAO 提案准备者整理、评估与分享公开证据包，识别重复信息来源，并选出当前材料中可区分的来源组合。

V1 的主要用户为：使用 GitHub 公开文档的开发者、研究协作者、DAO 提案准备者。新闻任意网页、电商、匿名消息和社交媒体爬取不是V1承诺。

反复使用场景：每次新提案、研究主题或证据包，重新提交与分享；材料更换/更新则产生新观察。V1不自动监控更新。

真实信任问题：材料提供者可用几个链接制造“多方独立佐证”的印象；研究协作者需要共享一份明确绑定输入材料、保留未知的关系评估，而不是各自聊天中的不同临时答案。

ChatGPT/普通服务器可以做分析，但默认没有链上共享引用、固定合约语义和网络独立验证生命周期。EchoMap的产品核心是可读取、可核验的共识记录，不以“更聪明的AI答案”作为价值。

### B2. Core User Flow

1. 整理一条claim，选择2–4份合规公开短文本材料，填写可选context。
2. 本地校验与排序；显示支持范围、公开性及钱包网络。
3. 生成/保存client_key、creator、payload；连接选择的浏览器钱包，切换Studionet。
4. 执行只读lookup，已存在同输入则打开原记录；无记录才准备交易。
5. 按匹配稳定SDK估计/提供协议费用参数；显示测试网GEN不足则引导免费Faucet，不要求购买。
6. 钱包签名并真实调用assess；立即保存GenLayer交易ID及request_id。
7. 跟踪网络状态、执行结果；不在Pending阶段显示假矩阵。
8. FINALIZED + successful后读finalized快照的get_assessment。
9. 显示矩阵、未知项和确定性最大两两独立集合；用户据此选材。
10. 分享公开结果URL；同事无需连接钱包即可核验输入、链上结果与关联交易。

产品闭环是“整理→评估→选材→协作分享”。不加入工作空间、成员邀请、账户系统、评论或后台数据服务。

### B3. Frontend Architecture

React + TypeScript + Vite，静态构建部署GitHub Pages，采用hash路由。依赖锁定，浏览器端打包SDK，不依赖运行时CDN、不需要Node服务器。

| 模块 | 责任 |
|---|---|
| 输入/表单 | 规范化、边界校验、样例加载；不判断正式关系 |
| 钱包adapter | 选择明确provider、连接/切换链、账户变更；私钥不进入应用 |
| GenLayer adapter | 稳定SDK、费用参数、write、transaction状态、finalized view |
| 生命周期controller | 每笔交易单一跟踪任务、读写错误分离、恢复与退避 |
| 结果呈现 | 链上schema校验、矩阵、集合、分享、原始来源与证据链接 |

只用React内置状态/少量hooks；不用Redux、复杂路由库、图布局库、大型UI组件库、索引器或后端。

localStorage仅作本机草稿/进行中请求恢复，不作为正式评估数据源或跨设备数据库。至多保存当前草稿和进行中的交易信息；公开报告按request_id访问，不做“我的全部历史”扫描。

### B4. Core Screens / UX

同一静态App，3个核心区域/视图：

| 区域 | 内容 |
|---|---|
| Start / Evidence Pack | 一句话用途、支持范围、真实已完成示例入口、claim/context/URL表单、连接与提交 |
| Transaction Progress | 请求/签名/已提交/等待/错误状态，真实交易ID，Explorer，暂停/恢复读取 |
| Shared Report | 只读来源列表、digest、矩阵、最大集合、UNKNOWN解释、复制链接、链上核验 |

只保留矩阵作为核心关系可视化，不另做力导向图、聚类视图或图动画。2–4个来源矩阵足以让审核员理解重复/独立/未知；颜色必须同时配标签，不靠色觉区分。

UI英文默认，提供中文切换；只有少量固定文案，enum值保持不变，来源原文不自动翻译。明亮简洁、强对比、直接说明用途；不使用交易所UI/K线、黑金风或复杂动画。

### B5. Wallet Flow

- 支持浏览器扩展钱包的EIP-1193连接；V1验收 MetaMask、OKX Wallet。两者共存时明确选择provider，不依赖含糊的window.ethereum抢占。
- 开始时不自动弹钱包；只读报告不要求钱包。
- 写入前确认chainId=61999、目标合约、当前账户；当前账户与签名前保存的creator必须匹配。
- 若链不存在，使用对应稳定网络参数add/switch；拒绝切链/签名是可恢复的用户取消。
- 签名前账户或链改变：阻止发送并重新确认；已发送后继续用只读RPC跟踪原交易，不因钱包断开清除它。
- 不要求WalletConnect、移动钱包跳转、登录系统或邮件验证。

### B6. Contract Interaction / On-chain State Reading

- 网络固定：Stable Studio/Studionet，61999，https://studio.genlayer.com/api，GEN，explorer-studio.genlayer.com。
- 单一canonical合约地址来自A部署清单，不创建Project专用第二个合约。
- 启动/打开报告时读取get_protocol_info一次；版本不匹配时显示配置问题，禁止write，不猜测兼容。
- 状态读取用稳定SDK对应的finalized快照语义；当前官方文档对应TransactionHashVariant.LATEST_FINAL。若托管版本语法不同，仅作同语义适配。
- 提交后轮询transaction，不在每个轮询周期重读完整合约状态。
- 成功finalized后读取目标Assessment；视图落后则只重试read，不重发write。
- RPC读取失败、found=false、配置错误、交易执行失败分别呈现。
- 分享路由：`#/report/<request_id>`，可带关联GenLayer tx ID；GitHub Pages不依赖服务器重写。
- 用户提供的关联tx只能在核验recipient、sender、method/inputs及生命周期后附加到报告。无法核验时只显示“未核实的关联交易”，不能提供multi-validator/创建证明标签。
- REUSED交易不意味着重新进行了AI分析。已验证首页示例使用实际NEW创建交易；其他关联交易明确标注重复调用或未知，不把重复成功receipt当成新共识证明。

### B7. Transaction Lifecycle

| UI状态 | 进入条件 | 用户反馈 / 可操作内容 |
|---|---|---|
| idle | 草稿/尚未write | 编辑、样例、查看已有记录 |
| requesting_wallet | 用户点击连接 | 提示在选定钱包确认；不显示已签名 |
| switching_network | 链不匹配 | 显示Studionet切换请求 |
| awaiting_signature | 交易准备完成 | 显示目标链、账户、动作及测试网费用 |
| submitted | 拿到真实GenLayer交易ID | 立即保存、显示链接 |
| pending | 网络处理中/尚无finality | 展示实际可证明状态；不能伪造validator进度百分比 |
| accepted_waiting_finality | 已接受但未FINALIZED | 明确等待最终确认；不作为最终报告分享 |
| finalized_reading | FINALIZED且执行成功 | 读取finalized业务记录 |
| finalized_complete | 记录COMPLETE | 展示完整分类，提醒不验证claim真伪 |
| finalized_partial | 记录PARTIAL | 展示合法UNKNOWN，允许新请求重新观察 |
| execution_failed | 真实执行/网络终态失败 | 原因、原交易、保留输入；允许确认后重试 |
| tracking_unavailable | RPC错误/429/等候超时 | 保留交易ID、暂停/继续读取，不说交易失败 |
| rejected_by_user | 用户拒绝签名/切链 | 返回可编辑状态，保留草稿 |

网络确切status名称以部署时锁定SDK/receipt为准，UI不造不存在的协议状态。UNDETERMINED/取消/拒绝等实际终态按成功检查映射；UNKNOWN仅为业务pair，不能用来代替共识失败。

统一成功条件：网络确认FINALIZED，execution success，finalized快照存在匹配request_id/payload/version的Assessment。三者缺一不得标记评估成功。

### B8. Rate Limits / Failure Recovery

- 每个页面最多一个进行中的transaction跟踪循环；请求不并发堆积。
- 初始约5秒一轮，长等待逐步延长到10–15秒；隐藏标签页暂停自动查询。
- 429遵守可见Retry-After；缺失时至少10秒退避，连续限流递增并适度jitter；所有读取共享冷却，不在多个组件各自retry。
- 返回错误数据可获得时保留并分类，不只凭英文message匹配“unknown RPC”。
- 长等待只暂停自动跟踪，用户可恢复；不承诺2–4分钟内交易一定FINALIZED。
- 有tx ID时先恢复该交易；无tx ID但可能发送过时，用已保存creator/key查询finalized记录并检查钱包/Explorer；found=false不证明旧交易不存在。
- 只有明确终态失败，或用户核查后主动重试，才重发原key；合约幂等兜底但不替代提交状态判断。
- 已存在PARTIAL的新观察必须新key；来源/claim修改后必须作为新请求，不占用旧key。
- 进行中账户切换、刷新、短暂断网不清除恢复信息；不启动第二个并行写流程。
- 已验证示例加载失败显示真实错误和Explorer入口；不能悄悄显示本地mock矩阵为链上结果。

### B9. External Data Flow

浏览器提交URL与claim/context；由Leader和Validator独立GET读取正文。前端不跨域抓正文、不转交未经链上独立获取的内容、不依赖外部API key。

报告来源链接用于用户自行核验；第三方网页变化不自动更新旧记录。样例元数据仅提供导航坐标，正式结果始终读链。

### B10. Demo Scenario / Demo Data

**受控样例：**4份短文本，全部标题注明SYNTHETIC DEMO。claim：2026-09-15，虚构Meridian公园白天气温超过30°C。

| Source | 冻结内容设计 | 预期关系 |
|---|---|---|
| A | 市政传感器第一手日志，给地点、采集时段、仪器与读数来源；情节明确虚构 | 与B依赖，与C有可见独立取得路径 |
| B | 使用A市政日志的社区报道，直接写明claim数据来自A；可改写措辞 | A–B=DEPENDENT |
| C | 志愿者独立温度计的现场记录；给自己取得数据的路径，说明未使用A数据 | A–C及B–C=INDEPENDENT |
| D | 仅重复“当天超过30°C”，未交代采集/引用来源 | 与A/B/C=UNKNOWN |

预期：6个pairs中1个D、2个I、3个U；PARTIAL；最大两两独立集合[A,C]，size=2。这个“2”来自synthetic材料中的显式取得路径，不证明真实世界存在对应观测。

样例内容每份远小于8,000字符；固定版本.txt路径，受控发布后不覆写。A仓库拥有独立fixture和说明；B可使用对应公开fixture并另放自己的可导航样例元数据。二者不得被称为4个独立网站。

**真实公开材料样例：**

- claim：ERC-20规范定义balanceOf用于返回指定账户的token余额。
- 来源1：ethereum/ERCs的ERCS/erc-20.md。
- 来源2：OpenZeppelin/openzeppelin-contracts v5.4.0的contracts/token/ERC20/IERC20.sol。
- 该OpenZeppelin接口自述实现ERC-20标准；判断范围是“规范规定的接口”，不是“这段代码是否独立开发”。两份材料发布者不同，仍对这一规范性claim共享ERC-20来源，预期DEPENDENT。
- 本次仅确认公开文本中可见相关内容，不代表已经用GenLayer完成评估。下一阶段须在Studionet真实运行后记录实际结果，不硬编码预期。
- 实施时将来源1的master导航URL固定到已核验commit SHA；来源2保留固定release tag。记录正文digest与发布来源。不得自行发明commit/hash。
- 若真实执行无法稳定分类或读取，不伪造通过；报告阻塞或改用同类真实权威原文与明确派生材料。任何改动不得改变规则或输入范围；更换具体材料属于数据绑定。

真实样例用于证明产品接触真实公开权威材料；受控样例用于稳定解释I/D/U和最大集合，两者明确分开。静态信息不要求伪装成“实时事实流”；每笔评估发生真实独立HTTP获取。

**2–4分钟演示：**

1. 首页打开已真实FINALIZED的受控样例，解释4个链接不等于4份独立证据。
2. 展示A–B重复、C的不同取得路径、D未知，以及选材集合。
3. 打开真实文档样例，说明不同发布者仍可能依赖同一规范来源。
4. 返回表单加载受控样例，连接钱包、签名新请求，展示真实交易跟踪。
5. 新请求若及时完成，展示finalized报告与分享；若仍pending，明确展示pending并回到预先验证的记录，不剪成假finality。

首页必须有“查看已验证链上示例”按钮，不要求审核员有历史记录、钱包余额或先执行一笔新交易。公开示例发布前必须实际验证，并将request_id、真实创建transaction、网络、合约坐标写入demo manifest。

### B11. Project Test Plan

| 范围 | 关键验收 |
|---|---|
| provider选择 | MetaMask与OKX单独/同时安装，选择正确钱包，不错用账户 |
| chain/account | 错链、拒绝切链、签名前改变账户被处理；已提交后继续读原交易 |
| 完整happy path | 钱包→真实assess→network lifecycle→finalized读取→矩阵→分享 |
| 成功条件 | Accepted不算Final；Finalized+execution error不算成功；finalized read落后只retry read |
| 幂等/recovery | 双击、刷新、有tx ID恢复、提交结果不明、原key冲突及PARTIAL新key |
| RPC限流 | 注入429/Retry-After，验证只有一个poller且不会触发write或并发读风暴 |
| 公开读取 | 无钱包打开已验证记录；同伴新浏览器看到同一finalized结果 |
| 显示诚实 | UNKNOWN、size0/1、source不可读、链下导航manifest与链上数据区分 |
| 关联证据 | 错误tx/不同合约/REUSED不冒充原始多验证者创建交易 |
| 安全渲染 | claim/context带HTML/指令，不执行脚本、不改变前端分类 |
| 发布 | GitHub Pages带仓库base路径与hash直达正常；移动窄屏可读；两语言核心状态齐全 |

自动测试主要验证adapter、状态机、恢复/限流、schema与请求一致性；真实钱包/网络由少量人工/浏览器验收补充。不用测试UI细枝末节或大型端到端钱包自动化框架。

### B12. Projects Submission Mapping

| 截图标准 | B提交证明 |
|---|---|
| 完整应用且GenLayer居于主流程 | 整理材料、真实write、跟踪、finalized呈现、选材和分享 |
| 真实信任问题 | 证据数量虚增、跨参与者共享来源关系，不以AI回答质量为主张 |
| 涉及事实时实时/权威数据 | 节点实际GET，真实ERC/OpenZeppelin公开来源，digest绑定；受控材料明确为虚构 |
| 完整源码和准确文档 | B源码、README、钱包/费用/来源限制、真实使用说明、部署与演示证据 |
| 前端实际调用并处理完整生命周期 | wallet/SDK适配、成功条件、finality、错误、恢复、429处理 |
| 区别基础模板且可持续使用 | claim相关矩阵、保守最大集合、共享记录，用户换主题/材料可再次提交 |
| 可体验演示/视频等加分材料 | GitHub Pages真实示例、新请求演示、2–4分钟视频计划；没有授权本轮发布帖子 |

提交B主URL为B仓库与公开GitHub Pages产品；注明使用A Primitive，提供真实调用证明、已验证只读结果和演示说明。A合约源码链接作为依赖说明，不能取代B自身完整产品源码。

## C. Scope Control — MINIMUM COMPLEXITY THAT STILL PASSES REVIEW

| 保留功能 | 删掉后会影响什么 |
|---|---|
| 一个核心合约、独立验证、稳定schema | 核心机制/GenLayer必要性/IC标准 |
| provenance积极证据与UNKNOWN | 结论正确表达，防止“没发现依赖=独立” |
| digest绑定 | 结果与证据对应；不同节点观察的可核验性 |
| 最大两两独立集合 | 产品选材价值与非传递关系处理 |
| 4方法中的lookup | 幂等恢复与避免重复交易 |
| 公共协议信息 | 版本错误时阻止错误调用 |
| 完整wallet/transaction/read流程 | Projects硬性标准 |
| 公开分享与已验证示例 | 跨方共享价值/审核首次体验 |
| 输入限制与source allowlist | 成本、稳定性、可测试性 |
| 费用参数与Faucet路径 | 真实可执行与0现金成本 |
| RPC退避/恢复 | 演示与持续使用可靠性 |
| 真实+受控样例 | 权威材料应用及短Demo可理解性 |

删除：后台、数据库、账户、成员系统、Workspace、社交功能、历史全链扫描、索引器、通用爬虫、浏览器正文代理、递归追溯、付费API、tokenomics、资金池、escrow、第二合约、管理员改结果、升级代理、自动监控、搜索、推送、PDF、截图OCR、AI摘要/翻译、置信度评分、事实核查、证据全文存链、复杂关系图/动画。

## D. Repository Strategy

计划仓库名为候选slug，创建时可因名称占用做等价重命名；不影响Primitive/Product名称与提交边界。

| | Repository A | Repository B |
|---|---|---|
| 建议slug | evidence-independence-matrix | echomap |
| 主交付 | 可复用GenLayer Primitive | 实际使用Primitive的完整小产品 |
| 必须包含 | 合约源码、protocol/spec、tests、fixtures、Studio示例、部署说明、README、license、版本锁定与部署清单 | React前端、adapter与UX测试、manifest/config、公开Pages、README、demo flow、提交证明与license |
| 独立审核 | 不运行B也能读懂、测试和部署A | B自己的源码/产品流程可审，不用A仓库冒充产品 |
| 不包含 | EchoMap UI、产品登录/页面、品牌业务状态 | 第二份可修改合约实现或第二部署地址 |

A拥有合约的单一源码真源；B通过部署地址、A source commit及schema引用它。B保留一份小的JSON部署配置和只读接口类型；不使用submodule、monorepo、多包发布或大型代码生成系统。

两个README分别解释用途和验收。A可包含指向EchoMap的可选应用案例链接，但主运行说明不能依赖B。

提交A/B使用各自不同主仓库URL；证明素材在对应仓库文档里集中引用，再按Portal实际表单添加。如果Portal实际限制某证据URL重复，提交前核实并保留各自主材料；不根据旧任务推断当前Portal的全局URL规则。

## E. WORK IMPLEMENTATION BUDGET

| 项目 | 复杂度 | 主要工作 / 预算控制 |
|---|---|---|
| Contract implementation | LOW-MEDIUM | 1合约、3记录结构、1write、3view；完整矩阵1主要共识路径，无资金与异步状态 |
| Frontend | MEDIUM | 钱包选择、签名、协议费用、finality、恢复/429；压缩为3视图，无图布局库/后台/历史索引 |
| Testing | MEDIUM | 验证错误Leader拒绝、非传递性、幂等、digest、故障/生命周期；有限mock+2真实样例，不建大型wallet自动化框架 |
| Documentation | LOW-MEDIUM | 两独立README+协议规范+共享部署事实；按各自提交边界裁剪，避免重复叙事 |
| Deployment | LOW-MEDIUM | 1次Studio部署、2仓库、免费Pages；绑定稳定版本、免费Faucet、真实多参与者和fee参数 |

没有HIGH。若实现中出现HIGH，先提出具体简化；不能为了方便而删除独立验证、未知语义、真实交易或恢复。上述是相对复杂度，不是精确token、工作时长、到账积分或审核通过率承诺。

V1目标为新增现金支出0：免费托管Studionet/内置Faucet、公开文本、开源工具、免费GitHub Pages；不采购API、RPC、数据库或GEN。Work自身订阅/额度是已有工具资源，不宣称免费无限使用。

Studionet钱包兼容层gas为0并不等于协议费用为0。部署/调用须使用稳定SDK与测试得到的fee profile/网络费用策略，必要GEN来自Faucet；不把费用参数全部硬编码为0。若免费额度/Faucet/托管provider不足，作为阻塞汇报，不能默认转付费或其他网络。

## F. PROJECT CHECKPOINT V1

### Overall Goal

零新增现金成本，在Stable Studionet建立可独立复用的EIM Primitive，并交付真实使用它的EchoMap；分别提交1个Intelligent Contracts与1个Projects。

### Current Stage Goal

冻结机制、信任边界、接口/状态、独立验证、数据范围、产品流程、仓库边界、测试与工作预算；不实现、不部署。

### Confirmed Decisions

- 用户已选择Evidence Independence Matrix方向。
- 两线共享核心合约，但分别可审；不沿用已完成项目。
- 官方文档支持当前稳定Studionet和custom Leader/Validator模式。
- 用户截图对IC强调独立Primitive/实质验证，对Projects强调真实信任问题、数据来源、完整实际交互和持续用途。
- 已核查ERC-20/OpenZeppelin公开短文本能表达真实规范来源例子；尚未在GenLayer运行。

### Frozen Decisions

| ID | 冻结内容 |
|---|---|
| F01 | Primitive EIM，Product EchoMap，协议EIM-V1-STUDIO，主标签开发者工具 |
| F02 | 仅Stable Studio/Studionet，61999；不用Bradbury、studio-dev或其他网络 |
| F03 | 一个核心合约，两独立仓库，A单一源码真源，B不部署第二合约 |
| F04 | 2–4份材料，1条claim，可选短context；一次原子评估路径 |
| F05 | INDEPENDENT/DEPENDENT/UNKNOWN，claim-scoped、对称、积极证据、非传递 |
| F06 | 不输出真实独立证据族总数；最大两两独立集合及I/D/U计数由确定性算法产生 |
| F07 | Source relevance、read_status、分析文本digest与全部pair构成共识实质字段 |
| F08 | 自定义validator独立fetch/完整分类，不用格式检查或convenience wrapper替换 |
| F09 | 1write+3view，sender/key幂等；同键不同payload拒绝；已存结果不改 |
| F10 | 3记录结构、1映射；不存业务Pending/Finalized、不写半成品 |
| F11 | GitHub允许host上的短UTF-8文本，无HTML/JS/PDF/递归追溯；大小及URL限制按A6/A13 |
| F12 | 内容不可读/不明与运行故障区分；共识失败不写“UNKNOWN成功报告” |
| F13 | React/TS/Vite静态Pages，3核心视图，矩阵可视化，少量中英文文案 |
| F14 | MetaMask+OKX扩展验收，明确provider，完整wallet/transaction/finality/read流程 |
| F15 | 成功=FINALIZED+execution success+匹配finalized记录；pending不显示假结果 |
| F16 | 单poller、429退避、刷新恢复；读取失败不重发write |
| F17 | 只读分享不需钱包；首页至少1个已真实验证示例；真实与synthetic材料分别标明 |
| F18 | 非传递/错误Leader/幂等/digest/错误恢复高价值测试，真实多参与者验收 |
| F19 | 无后台/数据库/账户/tokenomics/额外基础设施；费用靠免费测试资源 |
| F20 | 任何实质变更须ARCHITECTURE CHANGE REQUEST并由用户批准；本轮停止 |

A/B/C/D/E中明确的行为、限额、分类规则和验收条件同样是冻结规范，F表不是删去细节后的替代版。

### Completed Design

Primitive定义、复用方法、3种数据结构、4方法、状态转换、独立验证、canonical字段、集合算法、错误与幂等、数据规则、安全边界、Standalone Demo、产品用户/流程/UX、交易生命周期/恢复、两个样例设计、测试策略、两仓库边界、提交mapping与预算。

“Completed Design”仅指设计完成。尚无实际代码、仓库、部署地址、测试通过记录、交易hash、公开Demo或提交状态。

### Open Questions

仅剩实现/部署事实绑定，不能被用来重新设计产品：

1. Stable Studionet当前实际GenVM Depends标识、兼容genlayer-js/test SDK精确版本：实施第一步核实并锁定；不用“最新版本”替代“稳定兼容版本”。
2. 该托管环境的fee policy、Faucet和免费provider供给、真实参与者数量：在部署验证中测量，目标5/至少3；不能预先宣称完成。
3. 用户GitHub实际owner、仓库可用slug、Pages base URL与最终合约地址：在执行阶段绑定。
4. 真实样例source1具体commit SHA、各正文digest、两个NEW创建交易与request_id：真实运行后填写。

如稳定环境缺少必需功能或无法满足0新增成本/多参与者验收，这不是允许自动改设计的开放问题，必须汇报阻塞或提出ACR。

### Rejected Options

| 方案 | 原因 |
|---|---|
| 依赖图连通分量算独立证据族 | DEPENDENT不传递，计数会误导 |
| 域名/作者数或没有引用=独立 | 缺少积极provenance证据 |
| 普通ChatGPT输出直接存链 | 无独立实质验证，无法满足Primitive目标 |
| Validator只验格式或整体“差不多” | 不验证来源与逐pair决策 |
| UNKNOWN当失败或独立 | 混淆未知、共识故障和积极独立 |
| 自动把429/LLM失败转UNKNOWN | 伪装执行成功，污染不可修改结果 |
| 任意新闻URL通用爬虫 | 数据不稳定、HTML/渲染/限流成本超预算 |
| 每pair分别prompt/共识 | 放大费用、复杂度和一致性问题 |
| 后台缓存正文、数据库、链上历史扫描 | 不是核心闭环必需，增加实现/运行负担 |
| 聚类图/动画/评分/摘要 | 不影响核心验证，增加额度消耗或误导 |
| 修改旧报告/管理员强制结果 | 破坏可共享的稳定评估身份 |
| 两任务使用同一无法独立审核仓库 | 混淆提交边界 |

### Assumptions

稳定环境继续提供免费开发入口、免费Faucet与托管模型能力；GitHub与Pages免费用途适用；节点能访问允许host；用户材料可公开；来源取得路径是可见材料的声明，真实性不由本primitive证明。

### Constraints

无新增现金支出；仅Stable Studionet；1合约；2–4材料；1主要共识路径；少量state/method；静态前端；无私人秘密；不引用或复用旧项目；本轮不代码/不部署/不交接执行。

### Known Risks

- 独立性需要积极证据，真实资料可能大量UNKNOWN，产品必须诚实呈现。
- 来源声明可以造假，隐藏共同来源或相关模型偏差仍可能存在。
- Digest绑定保证材料一致性但使动态页面不易共识；V1用固定短文本控制。
- 限定GitHub文本缩小覆盖面，是为成本与稳定性作的有意V1限制。
- 固定URL/digest不等于全文归档；原文后来删除不可必然恢复。
- 托管环境、免费provider、Faucet、finality与RPC限流不可由产品保证。
- Reviewer可能仍把语义分类视为薄wrapper；必须用真实独立验证、非传递性/错误拒绝测试、可复用接口及产品闭环说明实质。
- 真实样例预期D尚未经链上验证；不能以预期代替实际结果。
- 评分和审核概率未经验证；本架构不承诺通过或积分。

### Next Step

停止在ARCHITECTURE FREEZE。等待用户单独要求生成WORK HANDOFF PACKAGE V1，再把本规范转为实现任务、冻结的逐字prompt、兼容性核查与验收步骤。此时仍不让Work重新参与产品设计。

## G. ARCHITECTURE CHANGE REQUEST

后续需要改变实质架构时，必须先提交：

| 字段 | 内容 |
|---|---|
| ACR ID | 唯一编号，关联受影响F编号和规范条款 |
| 原决定 | 原规则/接口/行为完整表述 |
| 问题 | 真实技术证据、用户需求或验证失败；“新模型想到更好点子”不是理由 |
| 新决定 | 明确替换内容，不使用模糊“优化” |
| 影响范围 | 合约语义、state/schema、测试、前端、提交材料、兼容性 |
| 增加实现成本 | LOW/LOW-MEDIUM/MEDIUM/HIGH及具体额外工作 |
| 迁移/风险 | 已部署记录、版本、案例与费用是否受影响 |
| 批准状态 | 未经用户明确批准不得实施 |

准确SDK版本锁定、同语义语法适配、实际地址/commit/URL/tx绑定、无语义影响的命名与排版不是ACR。若适配改变材料读取方式、equivalence、enum语义、成功条件、费用来源或多参与者标准，则必须ACR。

## 官方依据与已核查材料

以下链接用于核查，不表示本轮已部署或做过真实共识测试：

- [GenLayer Studio](https://docs.genlayer.com/developers/intelligent-contracts/tools/genlayer-studio)
- [Networks](https://docs.genlayer.com/developers/networks)
- [The Equivalence Principle](https://docs.genlayer.com/developers/intelligent-contracts/equivalence-principle)
- [Web Access](https://docs.genlayer.com/developers/intelligent-contracts/features/web-access)
- [Querying a Transaction](https://docs.genlayer.com/developers/decentralized-applications/querying-a-transaction)
- [Reading from Intelligent Contracts](https://docs.genlayer.com/developers/decentralized-applications/reading-data)
- [Studio Limitations](https://docs.genlayer.com/developers/intelligent-contracts/tools/genlayer-studio/limitations)
- [Fees and Transaction Policy](https://docs.genlayer.com/developers/decentralized-applications/fees-and-transaction-kit)
- [GenLayer JS official repository](https://github.com/genlayerlabs/genlayer-js)
- [GenLayer Test](https://docs.genlayer.com/api-references/genlayer-test)
- [ERC-20 primary text — navigation URL, to pin at implementation](https://raw.githubusercontent.com/ethereum/ERCs/master/ERCS/erc-20.md)
- [OpenZeppelin IERC20 — fixed release](https://raw.githubusercontent.com/OpenZeppelin/openzeppelin-contracts/v5.4.0/contracts/token/ERC20/IERC20.sol)

Portal审核映射来自用户本次提供的Intelligent Contracts / Projects截图；截图中的积分、额度或时间不是本项目成功保证。
