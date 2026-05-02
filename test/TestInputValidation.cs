using NUnit.Framework;

[TestFixture]
public class TestInputValidation
{
    [Test]
    public void TestSQLInjection()
    {
        string maliciousInput = "' OR 1=1 --";
        Assert.IsFalse(IsValidInput(maliciousInput));
    }

    [Test]
    public void TestXSS()
    {
        string xss = "<script>alert('hack')</script>";
        Assert.IsFalse(IsValidInput(xss));
    }

    public bool IsValidInput(string input)
    {
        return !(input.Contains("<script>") || input.Contains("' OR 1=1"));
    }
}