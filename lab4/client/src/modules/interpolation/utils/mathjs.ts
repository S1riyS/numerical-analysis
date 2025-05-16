import { all, create } from "mathjs";

export const configuredMath = create(all, {
  number: "number",
  precision: 32,
});
