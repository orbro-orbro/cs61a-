# Ants Vs. SomeBees 项目说明

本文结合项目网站与 ants.py 中的注释，按题目顺序整理每一题需要完成的功能、关键参数、重要变量含义，以及程序整体如何串起来。你可以把它当作做题路线图。

## Problem 00

### 这一题在做什么
- 先通读 ants.py，理解整个项目的对象关系和运行方式。
- 这是概念题，主要是确认你是否读懂了类、方法、变量和回合流程。

### 需要关注的参数和对象
- 这一题本身没有新增要实现的函数。
- 重点是理解后续所有题都会反复使用的基础对象：Place、Insect、Ant、Bee、GameState。

## Problem 01

### HarvesterAnt.action(self, gamestate)
- 功能：每回合给 colony 增加 1 点 food。
- 参数：
  - self：当前 HarvesterAnt 实例。
  - gamestate：当前游戏状态，用来访问和修改 food。

### HarvesterAnt 的重要属性
- food_cost：2
- health：1
- implemented：True

## Problem 02

### Place.__init__(self, name, exit=None)
- 功能：创建地点，并建立向左的 exit 连接，同时补上 entrance 反向引用。
- 参数：
  - self：当前 Place 实例。
  - name：地点名称字符串。
  - exit：该地点左侧相邻地点，默认是 None。
- 关键逻辑：如果当前 Place 有 exit，那么要把 exit 的 entrance 设成当前 Place。

### 这一题的核心变量
- exit：蜂移动时会沿这个方向往前走。
- entrance：蚂蚁搜索蜂时会沿这个方向往前看。

## Problem 03

### ThrowerAnt.nearest_bee(self)
- 功能：从当前 ThrowerAnt 所在地点开始，沿着 entrance 方向寻找最近的蜂，并返回一只随机蜂。
- 参数：
  - self：当前 ThrowerAnt 实例。
- 规则：
  - 如果当前地点有蜂，就从这里随机选一只。
  - 如果没有，就继续看 entrance 指向的下一个地点。
  - 不能返回 Hive 里的蜂。
  - 如果前方没有蜂，返回 None。

### ThrowerAnt 的基础属性
- damage：1
- food_cost：3
- health：1
- implemented：True

## Problem 04

### ShortThrower
- 功能：继承 ThrowerAnt，但只能攻击最多 3 格远的蜂。
- 参数：
  - 这一题没有新增方法参数，主要是修改类属性并复用 nearest_bee。
- 重要属性：
  - food_cost：2
  - health：1
  - upper_bound：3
  - lower_bound：0
  - implemented：True

### LongThrower
- 功能：继承 ThrowerAnt，但只能攻击至少 5 格远的蜂。
- 重要属性：
  - food_cost：2
  - health：1
  - lower_bound：5
  - upper_bound：float('inf')
  - implemented：True

### ThrowerAnt.nearest_bee 的范围变量
- lower_bound：允许攻击的最小距离，包含边界。
- upper_bound：允许攻击的最大距离，包含边界。
- ShortThrower 和 LongThrower 都依赖这两个边界控制射程。

## Problem 05

### FireAnt.__init__(self, health=3)
- 功能：初始化火蚁，默认生命值为 3。
- 参数：
  - self：当前 FireAnt 实例。
  - health：初始生命值，默认 3。

### FireAnt.reduce_health(self, damage_taken)
- 功能：火蚁受伤时会反弹伤害给同一地点的所有蜂；如果火蚁死亡，还会额外造成一次伤害。
- 参数：
  - self：当前 FireAnt 实例。
  - damage_taken：本次受到的伤害值。
- 关键点：
  - 先让父类处理自身扣血和死亡移除。
  - 再对当前地点的蜂造成反伤。
  - 迭代 bees 时要注意列表可能被修改，通常要先复制。

### FireAnt 的基础属性
- food_cost：5
- damage：3
- health：3
- implemented：True

## Problem 06

### WallAnt.__init__(self)
- 功能：创建墙蚁，作为高血量、无行动的防御单位。
- 参数：
  - self：当前 WallAnt 实例。

### WallAnt 的重要属性
- name：'Wall'
- food_cost：4
- health：4
- implemented：True

## Problem 07

### HungryAnt.__init__(self)
- 功能：初始化饥饿蚁，设置初始血量和冷却状态。
- 参数：
  - self：当前 HungryAnt 实例。
- 需要定义的实例变量：
  - cooldown：当前剩余咀嚼回合数，初始为 0。

### HungryAnt.action(self, gamestate)
- 功能：
  - 如果还在咀嚼，就减少 cooldown。
  - 如果不在咀嚼，就随机吃掉当前地点的一只蜂，并把 cooldown 设为 3。
- 参数：
  - self：当前 HungryAnt 实例。
  - gamestate：当前游戏状态。
- 关键点：
  - 吃蜂时是把蜂的 health 降到 0。
  - 没有蜂时什么也不做。

### HungryAnt 的重要属性
- name：'Hungry'
- food_cost：4
- health：1
- chew_cooldown：3
- implemented：True

## Problem 08a

### ContainerAnt.can_contain(self, other)
- 功能：判断容器蚂蚁是否还能装入另一只蚂蚁。
- 参数：
  - self：当前 ContainerAnt 实例。
  - other：待装入的蚂蚁。
- 规则：
  - 当前容器里不能已经有蚂蚁。
  - other 不能是容器蚂蚁。

### ContainerAnt.store_ant(self, ant)
- 功能：把 ant 存进当前容器。
- 参数：
  - self：当前 ContainerAnt 实例。
  - ant：要存放的蚂蚁。

### ContainerAnt.action(self, gamestate)
- 功能：如果容器里装着别的蚂蚁，就让它也执行 action。
- 参数：
  - self：当前 ContainerAnt 实例。
  - gamestate：当前游戏状态。

### ContainerAnt 的重要属性
- is_container：True
- ant_contained：被容纳的蚂蚁，初始为 None

## Problem 08b

### Ant.add_to(self, place)
- 功能：让蚂蚁加入地点时，支持容器蚂蚁和被容纳蚂蚁共存。
- 参数：
  - self：当前 Ant 实例。
  - place：要加入的地点。
- 规则：
  - 如果该地点没有蚂蚁，直接放入。
  - 如果已有蚂蚁，检查两只蚂蚁谁能容纳谁。
  - 如果能容纳，就让容器蚂蚁留在 place.ant，并把另一只存进去。
  - 如果都不能容纳，就抛出原来的 AssertionError。

### Place.ant 的重要规则
- 如果一个地点有两只蚂蚁，place.ant 必须指向容器蚂蚁。
- 被容纳的蚂蚁应该存在于容器蚂蚁的 ant_contained 中。

## Problem 08c

### ProtectorAnt.__init__(self)
- 功能：初始化防护蚁。
- 参数：
  - self：当前 ProtectorAnt 实例。
- 重要属性：
  - name：'Protector'
  - food_cost：4
  - health：2
  - implemented：True

### ProtectorAnt 的定位
- ProtectorAnt 是容器蚂蚁，但不负责输出伤害。
- 它的作用是保护同一地点里被容纳的蚂蚁。

## Problem 09

### TankAnt.__init__(self)
- 功能：初始化坦克蚁。
- 参数：
  - self：当前 TankAnt 实例。
- 重要属性：
  - name：'Tank'
  - food_cost：6
  - health：2
  - implemented：True

### TankAnt.action(self, gamestate)
- 功能：
  - 让被容纳的蚂蚁先执行 action。
  - 然后对同一地点的所有蜂造成 1 点伤害。
- 参数：
  - self：当前 TankAnt 实例。
  - gamestate：当前游戏状态。
- 注意：
  - 和 FireAnt、NinjaAnt 一样，攻击多个蜂时要注意列表可能被修改。

## Problem 10

### Water.add_insect(self, insect)
- 功能：把昆虫放进水里；如果该昆虫不防水，则立即把它杀死。
- 参数：
  - self：当前 Water 地点。
  - insect：要加入的昆虫。
- 处理顺序：
  - 先按普通方式把昆虫加入地点。
  - 再判断 insect.is_waterproof。
  - 如果不是防水的，把 health 降到 0。

### 需要新增/理解的变量
- Insect.is_waterproof：普通昆虫默认是 False。
- Bee.is_waterproof：True，因为蜂会飞。

## Problem 11

### ScubaThrower.__init__(self)
- 功能：创建潜水投手蚁，它和 ThrowerAnt 类似，但能在水里存活。
- 参数：
  - self：当前 ScubaThrower 实例。
- 重要属性：
  - name：'Scuba'
  - food_cost：6
  - health：1
  - implemented：True
- 关键点：
  - 它不应该因为进入 Water 而死亡。

## Problem 12

### QueenAnt.action(self, gamestate)
- 功能：
  - 女王像普通 ThrowerAnt 一样投掷。
  - 同时把她后方同一条 tunnel 上的蚂蚁伤害翻倍。
  - 每只蚂蚁只能被加倍一次。
- 参数：
  - self：当前 QueenAnt 实例。
  - gamestate：当前游戏状态。
- 关键点：
  - 可以借助 Ant.double() 来实现加倍。
  - 要从 queen 的 place.exit 一路向后遍历。
  - 容器蚂蚁和被容纳蚂蚁都要处理到。

### QueenAnt.reduce_health(self, damage_taken)
- 功能：女王死亡时触发 ants_lose()。
- 参数：
  - self：当前 QueenAnt 实例。
  - damage_taken：本次受到的伤害值。
- 关键点：
  - 先调用父类的扣血逻辑。
  - 如果女王死亡，就让蚂蚁失败。

### QueenAnt 的重要属性
- name：'Queen'
- food_cost：7
- health：1
- implemented：True

## Extra Challenge EC1

### SlowThrower.throw_at(self, target)
- 功能：对目标蜂施加减速状态。
- 参数：
  - self：当前 SlowThrower 实例。
  - target：被命中的蜂。
- 重要属性：
  - name：'Slow'
  - food_cost：6
  - health：1
  - implemented：True

### 需要理解的 Bee 行为
- 被减速的蜂在偶数回合正常行动。
- 在奇数回合不行动。
- 如果再次被减速，要从最新一次命中重新算持续时间。

## Extra Challenge EC2

### ScaryThrower.throw_at(self, target)
- 功能：让目标蜂害怕并后退，而不是前进。
- 参数：
  - self：当前 ScaryThrower 实例。
  - target：被命中的蜂。
- 重要属性：
  - name：'Scary'
  - food_cost：6
  - health：1
  - implemented：True

### Bee.scare(self, length)
- 功能：给蜂附加恐惧状态，让它尝试后退若干次。
- 参数：
  - self：当前 Bee 实例。
  - length：恐惧持续回合数。

## Extra Challenge EC3

### NinjaAnt.action(self, gamestate)
- 功能：对同一地点所有蜂造成伤害，但不阻挡路径。
- 参数：
  - self：当前 NinjaAnt 实例。
  - gamestate：当前游戏状态。
- 重要属性：
  - name：'Ninja'
  - food_cost：5
  - damage：1
  - health：1
  - implemented：True

### 相关基础变量
- Ant.blocks_path：普通蚂蚁默认会挡路。
- NinjaAnt.blocks_path：False，所以蜂会直接穿过去。
- Bee.blocked()：如果当前位置没有挡路蚂蚁，就返回 False。

## Extra Challenge EC4

### LaserAnt.__init__(self)
- 功能：初始化激光蚂蚁，并记录已经射中的昆虫数量。
- 参数：
  - self：当前 LaserAnt 实例。
- 重要属性：
  - name：'Laser'
  - food_cost：10
  - health：1
  - implemented：True
- 额外实例变量：
  - insects_shot：已经被激光实际伤害过的昆虫数量。

### LaserAnt.insects_in_front(self)
- 功能：收集当前激光蚂蚁同位置及前方所有昆虫，并记录每个昆虫和它的距离。
- 参数：
  - self：当前 LaserAnt 实例。
- 返回值：
  - 一个字典，键是 Insect，值是距离。

### LaserAnt.calculate_damage(self, distance)
- 功能：根据距离和已经命中的次数，计算这只昆虫应受到的激光伤害。
- 参数：
  - self：当前 LaserAnt 实例。
  - distance：目标昆虫距离 LaserAnt 的格数。

### LaserAnt.action(self, gamestate)
- 功能：对路径上的所有昆虫逐个造成伤害。
- 参数：
  - self：当前 LaserAnt 实例。
  - gamestate：当前游戏状态。
- 注意：
  - 伤害是逐个计算的，后面的目标会受到前面目标被击中后状态变化的影响。

## 贯穿全局的重要变量

### 位置和地图
- Place.exit：蜂前进方向的下一个地点。
- Place.entrance：蚂蚁朝前搜索蜂时的下一个地点。
- Place.bees：当前地点里所有蜂的列表。
- Place.ant：当前地点中的蚂蚁；若有容器蚁，通常指向容器蚁。
- Place.is_hive：是否是 Hive。

### 昆虫基础属性
- Insect.health：当前生命值。
- Insect.full_health：初始生命值。
- Insect.place：当前所在地点。
- Insect.damage：行动时造成的伤害。
- Insect.is_waterproof：是否可以进入水。

### 蚂蚁通用属性
- Ant.implemented：是否已经实现并可在 GUI 中使用。
- Ant.food_cost：放置花费。
- Ant.is_container：是否能容纳另一只蚂蚁。
- Ant.blocks_path：是否会挡住蜂。

### 游戏状态
- GameState.time：当前回合数。
- GameState.food：当前可用食物。
- GameState.places：所有地点的有序字典。
- GameState.bee_entrances：蜂可以进入 colony 的入口地点。
- GameState.active_bees：当前已经进入战场的蜂。
- GameState.ants：当前场上的所有蚂蚁。
- GameState.bees：当前场上的所有蜂。
- GameState.insects：当前场上的所有昆虫。

## 程序整体框架

### 核心对象关系
- 地点由 Place 串成 tunnel。
- 蜂从 Hive 出发，沿着 exit 往 Ant Home Base 推进。
- 蚂蚁放在某个 Place 里，通常沿着 entrance 朝前找蜂。
- 一个地点最多容纳一个普通蚂蚁；如果有容器蚁，可以同时放两只蚂蚁。

### 每回合流程
1. Hive 根据 AssaultPlan 放出新的蜂。
2. 玩家部署蚂蚁并消耗 food。
3. 所有活着的蚂蚁执行 action。
4. time 加 1。
5. 所有活着的蜂执行 action。
6. 蜂到达 AntHomeBase 则失败；蜂被全部消灭则胜利。

### 类的职责分工
- Insect：生命值、位置、死亡处理。
- Ant：放置、移除、容器支持、加倍逻辑。
- Bee：移动、攻击、状态效果。
- Place / Hive / AntHomeBase / Water：地图与特殊地形。
- GameState：统筹地图、时间、食物、回合和胜负。

## 运行与测试
- 解锁题目：python3 ok -q 题号 -u
- 检查答案：python3 ok -q 题号
- 启动 GUI：python3 gui.py
- 启动水域地图：python3 gui.py --water
- 指定初始食物：python3 gui.py --food 10

## 你在 ants.py 里最常改的地方
- Place.__init__
- Insect 的基础属性
- Ant.add_to / Ant.remove_from / Ant.double
- HarvesterAnt、ThrowerAnt、ShortThrower、LongThrower
- FireAnt、WallAnt、HungryAnt
- ContainerAnt、ProtectorAnt、TankAnt
- Water、ScubaThrower
- QueenAnt
- SlowThrower、ScaryThrower、NinjaAnt、LaserAnt
