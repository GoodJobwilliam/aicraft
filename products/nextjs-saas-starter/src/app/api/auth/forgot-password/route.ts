import { NextResponse } from "next/server";
import { db } from "@/lib/db";
import { sendPasswordResetEmail } from "@/lib/email";
import { absoluteUrl, generateToken } from "@/lib/utils";

export async function POST(req: Request) {
  try {
    const { email } = await req.json();

    if (!email) {
      return NextResponse.json(
        { error: "Email is required" },
        { status: 400 }
      );
    }

    // Always return success to prevent email enumeration
    const user = await db.user.findUnique({ where: { email } });

    if (user) {
      const token = generateToken();
      const resetUrl = absoluteUrl(`/reset-password?token=${token}&email=${email}`);

      // Store token in database (in production, use a proper reset tokens table)
      // For now, we just send the email
      await sendPasswordResetEmail({ email, resetUrl });

      console.log(`Password reset link for ${email}: ${resetUrl}`);
    }

    return NextResponse.json({
      success: true,
      message: "If an account exists with that email, a reset link has been sent.",
    });
  } catch (error) {
    console.error("Forgot password error:", error);
    return NextResponse.json(
      { error: "An unexpected error occurred" },
      { status: 500 }
    );
  }
}
