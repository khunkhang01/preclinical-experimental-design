# preclinical-experimental-design

`preclinical-experimental-design` คือ agent skill สำหรับออกแบบและตรวจสอบการทดลอง
preclinical แบบอิงหลักฐานและตรวจสอบย้อนกลับได้ ครอบคลุมงาน `in vitro`, `ex vivo`,
`in vivo`, pharmacodynamics/efficacy, toxicity/safety, PK/ADME, mechanism,
herbal/natural products และ formulation/drug delivery

จุดสำคัญของ skill นี้คือ ต้องทำ structured comprehensive literature review ก่อน
เสนอพารามิเตอร์ของการทดลอง ใช้ source hierarchy และ full-text verification สำหรับ
หลักฐานระดับพารามิเตอร์ สร้าง evidence matrix, quality appraisal, search-saturation
record และ audit trail ก่อนสรุปเป็น roadmap หรือ protocol

> **ขอบเขตความปลอดภัย:** skill นี้เป็น decision-support workflow ไม่ใช่สิ่งทดแทน
> approved SOP, institutional ethics/IACUC review, biosafety review, veterinary or
> clinical judgment หรือ regulatory advice ห้ามนำค่าที่ไม่ได้ตรวจสอบไปใช้เป็นคำสั่ง
> ปฏิบัติการ หากข้อมูลสำคัญไม่ครบ skill จะระบุ `UNRESOLVED` หรือ `PILOT-REQUIRED`
> และ block งานส่วนที่ได้รับผลกระทบ

## ความสามารถหลัก

- ค้นและสังเคราะห์หลักฐานอย่างเป็นระบบ พร้อมบันทึก query, แหล่งข้อมูล, วันที่ค้น,
  inclusion/exclusion และ citation chasing
- เปรียบเทียบวิธีการและพารามิเตอร์จากงานวิจัยระดับ full text
- สร้าง evidence matrix, quality appraisal, source manifest และ parameter-level citations
- วาง multi-stage roadmap พร้อม dependencies, go/no-go criteria และ phase-selection gate
- แสดง **ideal design** เทียบกับ **feasible design** พร้อมผลกระทบของข้อจำกัด
- ตรวจ feasibility, statistics/sample-size, reagent preparation, materials/equipment/
  consumables และ detailed protocol flowchart
- ใช้ deterministic Python utilities สำหรับการคำนวณ การตรวจสอบตาราง การ export CSV/XLSX
  และ visualization เมื่อมีประโยชน์
- ตรวจ Quality & Ethics Gate และ Citation Integrity Gate ก่อน finalize protocol

## Modes

| Mode | ใช้สำหรับ | จุดหยุดหลัก |
|---|---|---|
| **Review** | ทบทวนวรรณกรรม, evidence matrix, quality appraisal และ evidence gaps | หลัง Evidence Gate |
| **Roadmap** *(default)* | Review พร้อมแผนหลายระยะและเกณฑ์เลือก phase | หลัง Phase-selection Gate |
| **Protocol** | สร้าง protocol-ready design สำหรับ phase ที่เลือกแล้ว | หลัง Feasibility, Quality & Ethics และ Citation Integrity Gates |
| **Protocol Audit** | ตรวจ protocol เดิมและเสนอการแก้แบบติดตามได้ | หลัง audit และ gates ที่เกี่ยวข้อง |

ถ้าไม่ได้ระบุ mode ระบบจะใช้ **Roadmap Mode** และจะไม่ข้าม phase-selection gate
โดยอัตโนมัติ

## การติดตั้ง

Skill นี้เป็น package แบบ self-contained และไม่ผูกกับ platform ใดโดยเฉพาะ ให้เลือก
วิธีใดวิธีหนึ่งด้านล่าง

### วิธีที่ 1: ติดตั้งด้วย Git

แทนที่ `<skills-directory>` ด้วยโฟลเดอร์ skills ที่ agent ของคุณกำหนดไว้:

```bash
git clone https://github.com/khunkhang01/preclinical-experimental-design.git \
  <skills-directory>/preclinical-experimental-design
```

โครงสร้างที่ถูกต้องต้องเป็น:

```text
<skills-directory>/preclinical-experimental-design/
├── SKILL.md
├── README.md
├── scripts/
├── references/
└── assets/
```

`SKILL.md` ต้องอยู่ที่ root ของโฟลเดอร์ skill โดยตรง ไม่ใช่อยู่ในโฟลเดอร์ซ้อนอีกชั้น

### วิธีที่ 2: ดาวน์โหลด ZIP

1. เปิด repository นี้บน GitHub
2. เลือก **Code → Download ZIP**
3. แตกไฟล์ไปยังโฟลเดอร์ skills ของ agent
4. เปลี่ยนชื่อโฟลเดอร์ให้เป็น `preclinical-experimental-design` หากระบบแตกไฟล์
   แล้วเติม suffix เช่น `-main`
5. ตรวจสอบว่ามีไฟล์ `SKILL.md` อยู่ที่ root ตามโครงสร้างด้านบน

หลังติดตั้ง หาก agent ยังไม่เห็น skill ให้เริ่ม session ใหม่หรือ refresh รายการ skills
ตามวิธีของ platform นั้น แล้วเรียกชื่อ skill โดยตรงในคำขอ

## ตัวอย่างการเรียกใช้

```text
Use the preclinical-experimental-design skill in Roadmap mode.
Design an evidence-grounded preclinical program for [model], [intervention],
[comparator], and [primary endpoint]. Record assumptions, evidence gaps,
phase-selection criteria, and ideal-versus-feasible designs.
```

สำหรับงานเฉพาะ mode:

```text
Use preclinical-experimental-design in Review mode and produce the structured
literature review, search/saturation log, evidence matrix, quality appraisal,
source manifest, and parameter-level evidence gaps.
```

```text
Use preclinical-experimental-design in Protocol mode for the selected [phase].
Do not invent missing doses, concentrations, units, or sample-size inputs.
Run all applicable feasibility, Quality & Ethics, and Citation Integrity Gates.
```

```text
Use preclinical-experimental-design in Protocol Audit mode. Label every proposed
change KEEP, MODIFY, ADD, REMOVE, or UNRESOLVED and preserve the original value.
```

## Python utilities และ optional dependencies

การอ่าน `SKILL.md` และ references ไม่ต้องติดตั้ง Python เพิ่มเติม ส่วน utility scripts
ใน `scripts/` ใช้ Python 3 และรับ input ที่ผู้ใช้ประกาศอย่างชัดเจน:

| ไฟล์ | หน้าที่ |
|---|---|
| `evidence_matrix.py` | สร้าง ตรวจสอบ และ export evidence matrix |
| `sample_size.py` | คำนวณ sample-size approximation จาก input ที่ระบุ |
| `dilution_calculator.py` | คำนวณ dilution ด้วย `C1V1=C2V2` โดยไม่แปลงหน่วยเงียบ ๆ |
| `randomization.py` | สร้าง reproducible allocation จาก seed ที่ระบุ |
| `table_export.py` | export UTF-8 CSV เป็น XLSX |
| `validation_checks.py` | ตรวจ artifact ตาม mode ที่เลือก |
| `visualization.py` | สร้าง evidence heatmap เมื่อมี `pandas` และ `matplotlib` |

ติดตั้ง dependency เฉพาะเมื่อจำเป็นต้องใช้ความสามารถนั้น:

```bash
python -m pip install openpyxl pandas matplotlib
```

ตัวอย่างคำสั่งตรวจสอบที่ใช้บ่อย:

```bash
python scripts/evidence_matrix.py --help
python scripts/sample_size.py --help
python scripts/validation_checks.py --help
```

หมายเหตุ: utility scripts ช่วยเรื่องการคำนวณและ artifact QA เท่านั้น ไม่ได้ยืนยันว่า
สมมติฐานทางวิทยาศาสตร์ ขนาดผล ขนาดยา หรือ protocol ที่ได้เหมาะสมโดยอัตโนมัติ

## โครงสร้าง package

- [`SKILL.md`](SKILL.md) — agent contract, workflow state machine, gates, taxonomies
  และ output contract
- [`references/`](references/) — evidence policy, source provenance, quality appraisal,
  statistics, reagent preparation, ethics/regulatory และ output schema
- [`scripts/`](scripts/) — deterministic utilities สำหรับ calculation, validation,
  export และ visualization
- [`assets/`](assets/) — templates สำหรับ roadmap, protocol, audit, flowchart,
  evidence matrix, parameter table และ source manifest

## Mandatory outputs และหลักการ fail-closed

ผลลัพธ์ที่ต้องมีจะขึ้นกับ mode แต่โดยทั่วไปประกอบด้วย research-question record,
structured review, search/saturation log, evidence matrix, quality appraisal,
source manifest, parameter-level citations, confidence/status fields, evidence gaps
และ audit trail ส่วน Roadmap และ Protocol จะเพิ่ม roadmap, phase-selection gate,
feasibility gate, statistical plan, reagent/materials plan, flowchart และ quality/
ethics/citation gates ตามลำดับ

เมื่อ full text, หน่วย, model, safety context, calculation input หรือ approval ที่
สำคัญยังไม่พร้อม ให้ทำงานส่วนที่ไม่ถูก block ต่อได้ แต่ต้องแสดง blocker และ next action
อย่างชัดเจน ห้ามเปลี่ยนข้อมูลที่ขาดเป็นค่าที่ดูสมเหตุสมผล

## การอ้างอิงและการตรวจสอบ

เริ่มต้นจาก [`references/evidence_policy.md`](references/evidence_policy.md),
[`references/source_provenance.md`](references/source_provenance.md) และ
[`references/quality_appraisal.md`](references/quality_appraisal.md) สำหรับทุก mode
แล้วโหลด references เพิ่มตาม mode ที่ระบุใน `SKILL.md`

ก่อนนำ protocol ไปใช้จริง ผู้วิจัยต้องตรวจสอบ source full text, local SOP,
วัสดุ/อุปกรณ์จริง, ความปลอดภัย, ethics/biosafety และการอนุมัติจากหน่วยงานที่เกี่ยวข้อง
ด้วยตนเอง
