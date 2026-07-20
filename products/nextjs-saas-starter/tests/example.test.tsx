import { describe, it, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { Button } from "@/components/ui/button";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { cn, formatPrice, formatDate, truncate } from "@/lib/utils";

// ─── Utility Tests ─────────────────────────────────────────────

describe("Utility functions", () => {
  describe("cn", () => {
    it("merges class names correctly", () => {
      expect(cn("px-4", "py-2")).toBe("px-4 py-2");
    });

    it("resolves conflicts with tailwind-merge", () => {
      expect(cn("px-4", "px-6")).toBe("px-6");
    });

    it("handles conditional classes", () => {
      expect(cn("base", false && "hidden", "visible")).toBe("base visible");
    });
  });

  describe("formatPrice", () => {
    it("formats USD price correctly", () => {
      expect(formatPrice(29)).toBe("$29.00");
      expect(formatPrice(0)).toBe("$0.00");
      expect(formatPrice(99.99)).toBe("$99.99");
    });
  });

  describe("formatDate", () => {
    it("formats date string correctly", () => {
      const date = "2024-01-15T00:00:00.000Z";
      const result = formatDate(date);
      expect(result).toContain("January");
      expect(result).toContain("15");
      expect(result).toContain("2024");
    });
  });

  describe("truncate", () => {
    it("returns short strings as-is", () => {
      expect(truncate("Hello", 10)).toBe("Hello");
    });

    it("truncates long strings", () => {
      expect(truncate("Hello World This Is Long", 10)).toBe("Hello Worl...");
    });
  });
});

// ─── Component Tests ───────────────────────────────────────────

describe("Button", () => {
  it("renders with text", () => {
    render(<Button>Click me</Button>);
    expect(screen.getByText("Click me")).toBeInTheDocument();
  });

  it("renders with different variants", () => {
    const { container } = render(
      <Button variant="destructive">Delete</Button>
    );
    expect(container.firstChild).toHaveClass("bg-destructive");
  });

  it("handles click events", async () => {
    const handleClick = vi.fn();
    render(<Button onClick={handleClick}>Click</Button>);

    await userEvent.click(screen.getByText("Click"));
    expect(handleClick).toHaveBeenCalledOnce();
  });

  it("can be disabled", () => {
    render(<Button disabled>Disabled</Button>);
    expect(screen.getByText("Disabled")).toBeDisabled();
  });

  it("renders as a link when asChild is used", () => {
    render(
      <Button asChild>
        <a href="/test">Link</a>
      </Button>
    );
    expect(screen.getByText("Link")).toHaveAttribute("href", "/test");
  });
});

describe("Card", () => {
  it("renders with header, title, and content", () => {
    render(
      <Card>
        <CardHeader>
          <CardTitle>Test Card</CardTitle>
        </CardHeader>
        <CardContent>Card content</CardContent>
      </Card>
    );

    expect(screen.getByText("Test Card")).toBeInTheDocument();
    expect(screen.getByText("Card content")).toBeInTheDocument();
  });
});

describe("Badge", () => {
  it("renders with default variant", () => {
    render(<Badge>Default</Badge>);
    expect(screen.getByText("Default")).toBeInTheDocument();
  });

  it("renders with success variant", () => {
    render(<Badge variant="success">Active</Badge>);
    expect(screen.getByText("Active")).toBeInTheDocument();
  });
});
